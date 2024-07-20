'''sum = 0 
n = int(input('nhập n : '))
while n > 0 :
    a = n % 10 
    sum += a 
    n //= 10
print (sum) 
n = int (input('nhập n : '))
s = 0  
for i in range (1 , n+1) :
    if n % i == 0 : s += i 
print (s)
a = int(input())
b = int(input())
c = int(input())
if (a + b - c > 0) and (a + c - b > 0) and (b + c - a > 0) :
    if a == b == c :
        print ('tam giác đều')
    elif a == b or a == c or b == c :
        print ('tam giác cân')
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        print ('tam giác vuông')
    elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 - a**2 :
        print ('tam giác nhọn')
    else :
        print('tam giác tù')
else :
    print ('không phải tam giác')
a = int (input('nhập a : ')) 
b = int (input('nhập b : ')) 
print('a + b = ' , a + b)
print('a - b = ' , a - b) 
print('a * b = ' , a * b)
print('a chia lấy nguyên b ' , a // b) 
print('a mũ b ' , a ** b) 
if a > b :
    print ('a lớn hơn b')
elif a == b : 
    print ('a bằng b')
else : print ('a nhỏ hơn b')
print ('a AND b' , (a&b)) 
print ('a or b' , (a|b))
print ('a XOR b' , (a^b))
print (not (a == b)) 
print (a >> a) 
print (a << a)

n = int(input('nhập n : '))
s1 = 0
s2 = 0
for i in range (1 , 2*n+2 , 2) :
    s1 += i
for i in range (2 , 2*n+1 , 2) :
    s2 += (-1 *i)
print (s1 + s2)

n = int(input('nhập n : '))
s  = 0 
for i in range (1 , n+1) :
    s += (1 / i) 
print (s) 

from math import *
a = float (input())
b = float (input())
print ('phương trình bậc 2 một ẩn : a * x * x = b')
if (a * b > 0 ) :
    print ('phương trình có 2 nghiệm :' , sqrt (b/a) , 'và' , - sqrt (b/a))
elif (a == 0 or b == 0) :
    print ('phương trình vô số nghiệm')
else : 
    print ('phương trình vô nghiệm') 

n = int(input('nhập n : '))
FIBONACCI = [] 
a , b = 0 , 1 
for i in range (n) : 
    FIBONACCI.append(a)
    a , b = b , a + b
print (FIBONACCI) 

def KT (a) :
    s = 0 
    while (a > 0 ) :
        b = a % 10 
        s += b ** 3
        a = a // 10
    return s
n = int(input('nhập n : ')) 
l = []
for i in range (1,n+1) : 
    if KT(i) == i :
        l.append(i)
print(l)

def KT (a) :
    s = 0 
    for i in range (1 , a+1) : 
        if ( a % i == 0) :
            s += i 
    return s - a 
n = int(input('nhập n : '))
l = []
for i in range (1 , n+1) :
    if KT(i) == i :
        l.append(i)
print (l) 

N = int(input())
def KT (a ) :
    s = 0 
    for i in range (1 , a+1) :
        if a % i == 0 : 
            s += i 
    return s - a
l = []
for i in range (1 , N +1) :
    for j in range (i+1 , N+1) :
        if (KT(i) == j and KT (j) == i) :
            l.append ((i,j))
print (l)'''
