'''l =['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']
l_new = [int(l[i]) for i in range (len(l))]
sum = 0 
for i in l_new :
    sum += i
print (sum / len(l_new)) 

# bài 2 
A = set() 
B = set() 
a = int(input('nhập số học sinh đăng kí tại bàn 1 '))
b = int(input('nhập số học sinh đăng kí tại bàn 2 '))
for i in range (a) :
    A.add(int(input()))
print (A)
for i in range (b) :
    B.add(int(input()))
print (B)
print ('số học sinh đăng kí ở cả 2 bàn ' ,len( A & B))
print ('danh sách các sinh viên đăng kí của cả 2 bàn ' , list (A & B))
print ('danh sách các sinh viên đã đăng kí tại bàn 1 mà không ở bàn 2 ' , list (A - B)) 

# bài 3
n = int(input('nhập số phần tử mảng '))

m = int(input('nhập số phần tử của A và B '))

A = set()

B = set() 
l = []
for i in range (n) :
    l.append(int(input(f'nhập phần tử thứ {i+1} ')))
for i in range (m) :
    A.add(int(input()))
for i in range (m) :
    B.add(int(input()))
A_new = list (A) 
B_new = list (B)
sum = 0 
for i in range (n) :
    if l[i] in A : 
        sum += 1
    elif l[i] in B :
        sum -= 1
print ('tổng mức độ hạnh phúc' , sum)


# bài 4
S = set()

n = int(input('nhập số nguyên n '))
a = int(input('nhập số bạn chọn '))

for i in range (n) :
    S.add(int(input(f'nhập phần tử thứ {i+1} : ')))
s = list (S) 
sum = 0 
s_new = set()
for i in range (n) :
    if sum < a :
        sum += s[i] 
        s_new.add(s[i])
print (s_new) '''

# bài 5

l = []

n = int(input('nhập n '))

for i in range (n) :
    l.append(input())

b = tuple (l) 
dem = 0 
for i in b :
    if i.isdigit() :
        dem += 1
print (dem)
