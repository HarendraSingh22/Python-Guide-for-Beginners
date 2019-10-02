import datetime

# Print today.
print(datetime.date.today())
print(datetime.datetime.today())
print("")

# Generate date-type.
print(datetime.date(2019, 10, 03))
print(datetime.datetime(2019, 10, 03, 5, 30, 21))
print("")

# Extract date information.
today = datetime.datetime.today()
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
