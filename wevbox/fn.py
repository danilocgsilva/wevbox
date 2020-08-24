import os
import datetime


def create_first(prefix: str):

    path_to_create = os.path.join(prefix, hashtime())
    if not os.path.exists(path_to_create):
        os.makedirs(path_to_create)
    return path_to_create


def hashtime(working_date = None) -> str:
    if working_date == None:
        working_date = datetime.datetime.now()

    return str(working_date.year) + \
        str(working_date.month).zfill(2) + \
        str(working_date.day).zfill(2) + "-" + \
        str(working_date.hour).zfill(2) + \
        str(working_date.minute).zfill(2) + \
        str(working_date.second).zfill(2)

