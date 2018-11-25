
from functools import *

n=lambda a,b: a+a

result = n(3,4)

print(result)

nums = [3,5,6,8,4,89,90]

even = list(filter(lambda n: n%2==0,nums))

double = list(map(lambda a:a*2, even))

reduce = reduce(lambda c,d : c+d, double)

print(even)

print(double)

print(reduce)

