'''n = int(input('nhập n : '))

l = [int(input()) for i in range (n)] 

x = int(input('nhập x : '))

print('số lần xuất hiện của phần tử x : ' , l.count(x))

l[2 : 8] = [8,5,4,0,1,3]

print (l)

print ('số lớn nhất trong mảng là : ' , max (l))

print ('số nhỏ nhất trong mảng là : ' , min(l))

y = int(input('nhập y : '))

l.insert(0 , y)

print (l)

a = l.sort()

b = l.sort(reverse=True)

if (l == a) :
    print ('TĂNG')
elif (l == b ) :
    print ('giảm')
else : print ('NO')

N = []
sum = 0
for i in range (len(l)) :
    sum += l[i] 
    N.append(sum)
print (N)
m = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]

m.sort() 

print (m)

for i in range (len(m)) :
    m[i] = abs(m[i])

m.sort() 

print (m) 

# bài 2 :

k = int(input('nhập k : '))

a = [int(input()) for i in range (k)] 

n = int(input('nhập số dòng : '))

m = int(input('nhập số cột : '))

ma_tran = []

d = 0

if (n*m > k) :
    print ('NO')
else :
    for i in range (n) :
        hang = []
        for j in range (m) :
            hang.append (a[d])
            d += 1
        ma_tran.append(hang)
for hang in ma_tran :
    print (hang) 
# bài 3 :
s1 = input('nhập chuỗi s1 : ')

s2 = input('nhập chuỗi s2 : ')

for i in range (len(s1)-1 , -1 , -1) :
    print (s1 [i])

a = int(input('nhập a : '))

b = int(input('nhập b : '))

s2_list = list (s2)

print(s2_list)    

if (a >= 1 and a < b and b < len(s2_list)) :
    for i in range (len(s2_list)) :
        s2_list [a : b+1] = s2_list [a : b+1] [::-1]
    print (''.join(s2_list))
s3 = [s1[i] for i in range (len(s1)) if i % 2 != 0]
print (''.join(s3)) 
s1 = input('nhập chuỗi s1 :')
s2 = input('nhập chuỗi s2 : ')
s3 = ' ' 
max_len = max (len(s1) , len(s2)) 

for i in range (max_len) :
    if i < len(s1) :
        s3 += s1[i]
    if i < len(s2) :
        s3 += s2[i]
print(s3)
s1 = input('nhập chuỗi s1 :')
s2 = input('nhập chuỗi s2 : ')
if len(s1) > 1 and len(s2) > 1 :
    S1 = s2 [:2] + s1 [2:]
    S2 = s1 [:2] + s2 [2:]
elif len(s1) > 1 :
    S1 = s2 + s1[2:]
    S2 = s1[:2] +s2 
elif len(s2) > 1 :
    S1 = s2 [:2] + s1
    S2 = s1 + s2 [2:]
else :
    S1 = s2 + s1[1:]
    S2 = s1 + s2 [1:]
print (S1)
print (S2)

# bài 4
def ham_chuyen (s) :
    S = s.strip().lower().split()
    d = len(S) 
    for i in range (d) :
        S[i] = S[i].capitalize()  
    return ' '.join(S)
s = input('nhập chuỗi : ')
print (ham_chuyen(s)) '''

# bài 5 
n = int(input('nhập n : ')) 

l = list (map(int , input().split()))

Ba = []
d = 0
for i in range (n) :
    t = l[i] % 10 
    if t==1 or t==3 or t==5 or t==7 or t==9 :
        d+=1
        Ba.append(l[i])
print(d)
Ba.sort ()
print (Ba)
    