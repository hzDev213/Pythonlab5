
for i in range(10000,100001,10000):
    print("Iterations",i)
    pi= 0
    
    for j in range (1,i+1,1):
        pi= ((-1)**(i+1)/(2*i+1))
    pi *= 4
    print(pi)
