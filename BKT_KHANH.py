'''l = list (map (int , input().split()))

t = tuple (l)
d = set()
for i in t :
    if t.count(i) % 5 == 0 and t.count(i) % 10 != 0:
        d.add(i)
print (d) 

# bài 2

x = int(input('nhập địa điểm cần phải đến : ')) 

if (x%3 == 0) :
    print ('số bước tối thiết là : ' , x // 3)
else : print ('số bước tối thiểu là : ' , (x // 3) +1)


# bài 4 :

l = list (input())

s =set(l)
s.remove(' ')
print (s)
'''
# bài 5

n = int (input())

l = [int(input()) for i in range (n)]

l.sort() 

print (l[-1] + 1)