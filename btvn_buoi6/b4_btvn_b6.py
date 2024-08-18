

n = int(input())

def ham (c) :
    dem = 0
    while (c >= 10) :
        sum = 0
        while (c>0) :
            d = c %  10 
            sum += d
            c //= 10
        c = sum 
        dem += 1
    print (c)
    print (dem+1)
ham(n)