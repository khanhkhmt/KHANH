chuoi = input('nhập chuỗi : ') 

d = {} 

for i in chuoi : 
    if i in d :
        d[i] += 1
    else :
        d[i] = 1
        
print (d)