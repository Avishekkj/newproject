
import sys

sys.getrecursionlimit(1500
                      )
print(sys.getrecursionlimit())


def fact():
    n =int(input("enter a value "))
    x=1
    for a in range(1,n+1):
            x = x*a

    return x

result = fact()

print(result)



