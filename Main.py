from datetime import date,time,datetime
import pytz
import time as t
local_time = t.tzname[0]
# Get current date
today=date.today()
# Get current time
now = datetime.now()
print("The current date is:", today)
print("The current date and time is:", now)
print("Detected timezone is:", local_time)