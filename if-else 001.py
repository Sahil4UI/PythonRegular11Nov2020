'''
number = int(input("Enter a number:"))
if number%2 == 0:
    print("even")
else:
    print("odd")
'''
'''
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))

if  number1>number2:
    print(number1,"is greater")
elif number1==number2:
    print(number1,"==",number2)
else:
    print(number2,"is greater")
'''
'''
a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = int(input("Enter number3:"))

if a>b and a>c:
    print(a,"is largest")
elif b>c:
    print(b,"is largest")
else:
    print(c, "is largest")
'''
#input 3 sides of traingle and check wether traingle is equilateral, isoceles or scalene

a = int(input("Enter side1:"))
b = int(input("Enter side2:"))
c = int(input("Enter side3:"))

if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print("equilateral")
    elif a==b or a==c or b==c:
        print("isoceles")
    else:
        print("scalene")
else:
    print("not a valid traingle")



    





    
