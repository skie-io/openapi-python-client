import datetime
from typing import cast, Union

some_source = date(2020, 10, 12)
some_destination = some_source if some_source else None 
_a_prop = some_destination
a_prop: Optional[datetime.date]
if _a_prop is None:
    a_prop = None
else:
    a_prop = str_to_date(_a_prop)


