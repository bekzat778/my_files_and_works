import datetime

d = datetime.date(2015,8,15)
d1 = datetime.date(2015,8,16)
dt = d1-d


print(dt.total_seconds())