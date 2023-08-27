import requests
import calendar

# This section gets the "steps.txt" file from the internet and saves it to our computer
url = "https://raw.githubusercontent.com/remjw/data/master/py_programming_data/steps.txt"
response = requests.get(url)
if response.status_code == 200:
    with open('steps.txt', 'wb') as f:
        f.write(response.content)
else:
    print("Failed to download the file.")
    exit()

# We are preparing to count how many steps we have in total and on how many days
total_steps = 0
days = 0

print("---- 2023 ----")

# We start at the first month (January) and go until the last month (December)
month_number = 1
while month_number <= 12:
    
    # Here we figure out how many days are in this month
    if month_number in (4, 6, 9, 11):  # These months have 30 days
        days_in_month = 30
    elif month_number == 2:  # February has 28 days (because it's not a leap year)
        days_in_month = 28
    else:  # All other months have 31 days
        days_in_month = 31

    # Now, for each day in the month, we want to find out how many steps were taken
    steps_for_month = 0
    for _ in range(days_in_month):
        with open('steps.txt', 'r') as file:
            for _ in range(days):  # This skips the days we've already read
                file.readline()  
            daily_steps = int(file.readline())  # This gets the steps for today
        steps_for_month += daily_steps  # Add today's steps to the month's total
        total_steps += daily_steps  # Add today's steps to the year's total
        days += 1  # We count one more day

    # Calculate the average steps for this month
    average_steps = steps_for_month / days_in_month
    print(f"Month {month_number} ({days_in_month} days) : {average_steps:.1f} steps per day")
    
    # Go to the next month
    month_number += 1

# Finally, we calculate the average steps for the whole year
yearly_average = total_steps / days
print(f"\nYearly average steps per day during {days} days: {yearly_average:.1f} steps per day")
