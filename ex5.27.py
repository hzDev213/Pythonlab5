
for i in range(10000,100001):
    pi= 3.14
    piCount = 1
    j = 1
    sum = 1
    for j in range (j,i):
        piCount= ((-1)**(j+1)/(2*j+1))
        sum += piCount
    pi *= sum
    print(pi)