year = int(input("Enter the year: "))
first_day = int(input("Enter the first day of the year: "))


days_of_week = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

if year % 4 == 0:
    days_in_month[1] = 29


for month in range(12):
    print(f"1 {months[month]} {year} of year {days_of_week[first_day]}.")
    first_day = (first_day + days_in_month[month]) % 7
