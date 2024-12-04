check = 0 
for i in range (33,127):
    b = chr(i) # принимает целое число и возвращает соответствующее ему символ, промежуток 33 до 127
    print(b, end=" ")
    check += 1
    if check == 10:
        print()
        check = 0