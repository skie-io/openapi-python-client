import datetime
from typing import cast, Union

{% from "property_templates/date_property.py.jinja" import transform, construct %}
some_source = date(2020, 10, 12)
{{ transform(property, "some_source", "some_destination") }}
{{ construct(property, "some_destination") }}
