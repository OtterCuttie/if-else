# import random
# rn=random.randint(0,10)
# for i in range(5):
#     b= int(input('Введите число, которые, как вы думаете, загадал комп: '))
#     if(rn>b):
#         print('Меньше загаданого')
#     elif(rn<b):
#         print('Больше загаданого')
#     elif(rn==b):
#         print('МОЛОДЕЦ')
#         break
    
# GAME=True
# count=5
# while GAME:
#     print(count,"попыток/пытка")

#     b= int(input('Введите число, которые, как вы думаете, загадал комп: '))
#     if(rn>b):
#         print('Меньше загаданого')
#     elif(rn<b):
#         print('Больше загаданого')
#     elif(rn==b):
#         print('МОЛОДЕЦ')
#         GAME=False
#     if(count<=0):
#         print("you lose")
#         GAME=False
#     count-=1
# a=int(input('a'))
# b=int(input('b'))
# def pupu (a,b):
#     return a+b

# sum=pupu(a,b)
# print (sum)
# n=int(input('n '))
# def taxi(n):
#   bill= 85+15*(n//200)
#   print (bill)

# taxi(n)
# import random
# mass=[]
# for i in range(10):
#     mass.append(random.randint(0,10))

# print (mass)
n=int(input('от какого до какого'))
def uuuuuu():
    mass=[]
    if(n>=0):
        for i in range(n,0,-1):
            mass.append(i)
        for i in range(2,n+1,1):
            mass.append(i)
        print(mass)
    else:
        for i in range(n,0,1):
            mass.append(i)
        for i in range(2,n+1,-1):
            mass.append(i)
        print(mass)
    

uuuuuu()
