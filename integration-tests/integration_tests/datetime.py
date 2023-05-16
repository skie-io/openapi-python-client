import datetime
import sys
from typing import Union


def str_to_date(date_or_str: Union[datetime.date, str]) -> datetime.date:
    if isinstance(date_or_str, str):
        return datetime.date.fromisoformat(date_or_str)
    else:
        return date_or_str


if sys.version_info >= (3, 11):

    def str_to_datetime(datetime_or_str: Union[datetime.datetime, str]) -> datetime.datetime:
        if isinstance(datetime_or_str, str):
            return datetime.datetime.fromisoformat(datetime_or_str)
        else:
            return datetime_or_str

else:

    def str_to_datetime(datetime_or_str: Union[datetime.datetime, str]) -> datetime.datetime:
        if isinstance(datetime_or_str, str):
            return datetime.datetime.fromisoformat(datetime_or_str.rstrip("Z")).replace(tzinfo=datetime.timezone.utc)
        else:
            return datetime_or_str
