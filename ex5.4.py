print ("Miles to Kilometers Table")
print ("---------------------------")
print (format("Miles", "10s"), format("Kilometers", "<15s"))
for i in range (1, 11):
    print(i, "            ", (i * 1.609))