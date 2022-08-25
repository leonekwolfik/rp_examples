# baktun2.py
from datetime import datetime
from zoneinfo import ZoneInfo

from dateutil.relativedelta import relativedelta

yucatan_tz = ZoneInfo("America/Merida")
BAKTUN = datetime(year=2012, month=12, day=21, hour=23, minute=59, second=59,
    tzinfo=yucatan_tz)
now = datetime.now()
local_now = now.astimezone()

survived = relativedelta(local_now, BAKTUN)
output = []

for time_unit in ["years", "months", "days", "hours", "minutes", "seconds"]:
    unit = getattr(survived, time_unit)
    if unit != 0:
        time_unit = time_unit[:-1] if unit == 1 else time_unit
        output.append(f"{unit} {time_unit}")

output = ", ".join(output)

print(f"It is currently:", now.strftime("%A, %B %d, %Y at %H:%M %p %Z"))
print(f"You have survived {output} since the Mayan Bak'tun!")
