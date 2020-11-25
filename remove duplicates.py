'''
x=[1,1,1,2,2,2,3,3,3,4,5,6]
#x=[1,2,3,4,5,6]
y=[]

for number in x:
    if number not in y:
        y.append(number)

print(y)
'''
"""
x=[1,1,1,2,2,2,3]
for number in x:
    if x.count(number) == 1:
        print(number)
        break
"""
"""
x = [1,2,3,4,5,6,8,9,10]

add1 = sum(x)
add2=0
for i in range(min(x),max(x)+1):
    add2+=i

print(add2-add1)
"""

x = [[1,2],
     [3,4]]

y = [[5,6],
     [7,8]]

result = [[0,0],
          [0,0]]

for i in range(2):
    for j in range(2):
        result[i][j] = x[i][j]+y[i][j]
        
        



























