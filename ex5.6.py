MILE_TO_KM = 1.609
KM_TO_MILE = 0.621

print(format("Miles", "10s"), format("Kilometers", "15s"), "|", format("Kilometers", "15s"), format("Miles", "10s"))

for i in range(1, 11): 
    miles = i
    kilometers_from_miles = miles * MILE_TO_KM
    
    kilometers = 20 + (i - 1) * 5 
    miles_from_kilometers = kilometers * KM_TO_MILE
    
    # Вывод строки таблицы
    print(format(miles, "<10"), format(kilometers_from_miles, "<15"), "|", format(kilometers, "<15"), format(miles_from_kilometers, "<10"))