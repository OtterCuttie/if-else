print("flower")
name='gogo'

a=(int(input('первая сторона')))
b=(int(input('вторая сторона')))
c=(int(input('третья сторона')))
if(a+b>c and a+c>b and b+c>a):
    print('такой треугольник существует')
else:
    print('не сущетсвует такого треугольника')

