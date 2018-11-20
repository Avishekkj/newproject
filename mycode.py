from array import *
from array import ArrayType


vals = array('i' , [1,2,3,4,5])

name = array('u', 'avishek')

vals.reverse()
print(vals)
name.reverse()
print(name)

arr = array('i', [])
n =int(input("enter a length"))

for i in range(n):
    x= int(input('enter values'))
    arr.append(x)

print(arr)

ser: int = int(input('enter the value to search'))
k=0
for e in arr:
    if e==ser:
        break;
    else:
        k =k+1

print(k)




arr = array('i', [4, 5, 6, 3, 2])

# x: =len(arr)

arr1 = array('i', [])
#
# arr1 = arr.reverse()
k=0
for e in arr:
    arr1.append(e)
    k = k + 1
    if k==2:
        break

print(arr1)




