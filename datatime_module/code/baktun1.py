# baktun1.py
from datetime import datetime

BAKTUN = datetime(year=2012, month=12, day=21, hour=23, minute=59, second=59)
survived = datetime.now() - BAKTUN

print(f"You have survived {survived} since the Mayan Bak'tun!")
