import time
timestamp=time.strftime("%H:%M")
print(timestamp)
hours,minutes =map(int,timestamp.split(":"))

if hours>6 and hours <12:
  print("Good Morning!")
elif hours >=12 and hours <15:
  print("Good Afternoon!")
elif hours >=15 and hours<18:
  print("Good Evening!")
else:
  print("Good Night!")



#Using timezone
"""from datetime import datetime
import pytz

utc_zone=datetime.utcnow()
eastern_zone=pytz.timezone('US/Eastern')
dc_time=utc_zone.astimezone(eastern_zone)

dc_hour=dc_time.hour
print("Current time in DC is:",dc_hour)

if dc_hour>6 and dc_hour <12:
  print("Good Morning!")
elif dc_hour >=12 and dc_hour <15:
  print("Good Afternoon!")
elif dc_hour >=15 and dc_hour<18:
  print("Good Evening!")
elif dc_hour>=18 and dc_hour<6:
  print("Good Night!")"""