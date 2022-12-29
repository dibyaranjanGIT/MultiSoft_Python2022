import datetime

date = datetime.datetime.now()
print(date.year)
print(date.month)

day_of_week = date.weekday()
print(day_of_week)

# Create your own datetime object
new_date = datetime.datetime(year=2023, day=10, month=1, hour=4)
print(new_date)