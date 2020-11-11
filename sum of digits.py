number = int(input("Enter a number : "))
result = 0

for i in range(len(str(number))):
    rem = number%10
    result = result+rem
    number = number//10
    
print(result)


#check wether number is armstrong number or not
#find the reverse of number->123->321
#fibonacci series 0 1 1 2 3 5 8....
