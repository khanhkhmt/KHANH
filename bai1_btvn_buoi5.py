n = int (input('nhập số sinh viên'))

d = {int(input('nhập msv : ')) : int(input('nhập điểm : ')) for i in range (n)}

d [2024500694] = 5

k = {key for key , value in d.items() if value < 2 }
for key in k :
    del d[key]
print (d)