# - Syntactical Error
# - run time Error - > exception ->
try :
    x = int(input("Enter first number : "))
    y = int(input("Enter Second Number : "))

    a = x+y
    b = x-y
    c = x*y
    d = x/y

    # list1 = [1,2,3,4,5]
    # print(list1[1000])
    # print("Sum = ",a)
#     print("difference = ",b)
#     print("product =12 ",c)
#     print("division = ",d)

except BaseException as be:
    print(be)
finally:
    print("****PRogram ended successfully*******")

# else:
#     print("Sum = ",a)
#     print("difference = ",b)
#     print("product =12 ",c)
#     print("division = ",d)





'''
except ZeroDivisionError:
    print("Denominator is Zero, can't divide")
except ValueError:
    print("invalid value")
except IndexError:
    print("invalid index")
'''