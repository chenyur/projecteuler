import datetime

oneday = datetime.timedelta(days = 1)

start = datetime.date(year = 1901, month = 1, day = 1)

mondays = []

while start.year != 2001:
    if start.weekday() == 6 and start.day == 1:
        mondays.append(start)
    start += oneday

for m in mondays:
    print m

print len(mondays)
