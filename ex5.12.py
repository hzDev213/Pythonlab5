check = 0 #* счетчик на количество чисел в строке 
for num in range(100, 1001):
    if num % 5 == 0 and num % 6 == 0:
        print(num, end=" ")
        check += 1
        if check == 10:  # * если в строке 10 чисел то переход на новую
            print()
            check = 0
