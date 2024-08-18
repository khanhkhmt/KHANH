n = int (input('nhập số hàng : '))
m = int (input('nhập số cột : '))
l = []
def ham(n , m , l ) :
    for i in range (n) :
        h = []
        for j in range (m) :
            h.append(int(input()))
        l.append(h)
    return l
l1 = []
def ham1 (n , m ,l , l1) :
    ham(n,m,l)
    for i in range (m) :
        h1 = []
        for j in range (n) :
            h1.append(l[j][i])
        l1.append (h1)
    return l1
print (ham1(n,m,l ,l1))
print (ham(n,m,l))