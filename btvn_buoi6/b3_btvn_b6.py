def caculate (operation , *args ) :
    if (operation == 'add') :
        sum = 0 
        for i in args :
            sum += i
        return sum
    elif (operation == 'multiply') :
        tich = 1 
        for i in args :
            tich *= i
        return tich
    elif (operation == 'max') :
        return max(args )
    elif (operation == 'min' ) :
        return min(args )
    else : return 'invalid operation'
print (caculate('add' , 1 , 2 , 3))