import calendar

year = int(input("Enter the year: "))
firstDay = int(input("Enter the first day of the year: "))


cal = calendar.TextCalendar(firstDay)  # Создаем объект TextCalendar с заданным первым днем недели
for month in range(1, 13):
    print(cal.formatmonth(year, month))
