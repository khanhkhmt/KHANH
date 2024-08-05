a = tuple()
a = list(map(int, input().split()))
b = list(set(a))
kt = 0
for i in b:
    if a.count(i) % 5 == 0 and a.count(i) % 10 != 0:
        print(i)
        kt = 1
if kt==0:
    print('khong co')
a = tuple()