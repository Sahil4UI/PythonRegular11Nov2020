'''
number = int(input("Enter a number : "))

for i in range(2,number):
    if number%i==0:
        print(number,"is not prime")
        break
else:
    print(number,"is prime")
'''
#find the sum of numbers from 1-10
result=0
for i in range(1,11):
    result=result+i
print(result)
    
