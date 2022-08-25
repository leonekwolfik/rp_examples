# baktun2.py
from datetime import datetime
from zoneinfo import ZoneInfo

yucatan_tz = ZoneInfo("America/Merida")
BAKTUN = datetime(year=2012, month=12, day=21, hour=23, minute=59, second=59,
    tzinfo=yucatan_tz)

now = datetime.now()
local_now = now.astimezone()
survived = local_now - BAKTUN

print(f"You have survived {survived} since the Mayan Bak'tun!")
