import datetime as d
import pytz
t=d.date.today()
# print(t)
b=d.date(2002,10,10)
# print((t-b).days)
tdelta=d.timedelta(days=26)
# print(b+tdelta)
a=d.datetime.now(tz=pytz.UTC)
b=a.astimezone(pytz.timezone('Indian/Kerguelen'))
# print(b)
# datetime string formatting
# print(b.strftime('%d %B %Y'))
print(d.datetime.strptime('06 May 2020','%d %B %Y'))

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)