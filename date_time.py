import datetime
from datetime import time

current_date = datetime.datetime.now()
print(current_date)
print(current_date.day)
print(current_date.month)
print(current_date.year)

random_date = datetime.datetime(2024, 8, 17)
print(random_date)

# Getting DateTime from Timestamp
date_time = datetime.datetime.fromtimestamp(1576639468)
print("Datetime from timestamp:", date_time)

my_time = time(13, 24, 56)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

time_in_one_year = current_date + datetime.timedelta(days=365)
print(time_in_one_year)

base = datetime.datetime.today()
num_days = 10

# Create a range of Dates with start date known
date_list = [base - datetime.timedelta(days=x) for x in range(num_days)]
print(date_list)
