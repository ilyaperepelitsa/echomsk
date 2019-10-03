from random import randint

# from sqlalchemy.sql import select
from sqlalchemy.sql import exists
from sqlalchemy import and_
from echomsk.models import Errors, DupUrlErrors


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    return dat

def log_error(bmid, nid, error_type, session):

    error_exists = session.query(exists().where(and_(
                    Errors.bmid == bmid,
                    Errors.nid == nid,
                    Errors.error_type == error_type)
                )).scalar()

    # error_exists = False
    if not error_exists:
        error_entry = {"bmid" : bmid, "nid" : nid, "error_type" : error_type}
        adding_error = Errors(**error_entry)
        session.add(adding_error)
        session.commit()

def log_url_error(url, session):
    error_exists = session.query(exists().where(
                    DupUrlErrors.url == url
                )).scalar()

    if not error_exists:
        error_entry = {"url" : url}
        adding_error = DupUrlErrors(**error_entry)
        session.add(adding_error)
        session.commit()
