import calendar
from datetime import datetime
year = int(datetime.now().year)
month = int(datetime.now().month)
cal = calendar.month(year,month)
print(cal)