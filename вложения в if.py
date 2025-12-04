a=int(input())
print(a)                                                
if a%5==0:
    if a>9 and a<100:
        print(1)
        print(2)
    else:
        print(3)
        print(4)
else:
    if a%2==0:
        print(5)
        print(6)
    else:
        print(7)
        print(8)
print ("end")
'поиск минимального значения'
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if b>c:
        print(c)
    else:
        print (b)
else:
    if a>c:
        print(c)
    else:
        print(a)
        
'в какую четверть попадет точка с указанными кординатами'
print('Ведите значение Х')
x=int(input())
print('Ведите значение y')
y=int(input())
if x==0 and y==0:
    print ('центр координат')
else:
    if x>0:
        if y>0:
           print(1)
        else:
           print(4)
    else:
        if y>0:
            print(2)
        else:
            print(3)

print('end')