from datetime import date
from typing import cast, Union

some_source = date(2020, 10, 12)
some_destination = some_source.isoformat()
a_prop = str_to_datetime(some_destination)


