#!/usr/bin/env python3

import pytz
from datetime import datetime

try:
    time_zone = pytz.timezone("UTC")
except pytz.exceptions.UnknownTimeZoneError:
    print("Not a valid TZ")

time = pytz.utc.localize(datetime.now()).astimezone(time_zone)
print(time.strftime("%b %d, %Y, %-I:%M:%S %p"))
