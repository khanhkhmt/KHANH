n = int(input())
a = list(map(int,input().split()))
k = int()
i = int()
if a[0] == 1:
    k = 2
else:
    k = 2
while i < n:
    if a[i] != k+1:
        k += 1
    else:
        k = a[i] + 1
    i += 1
print(k)