import math 

def divSum(n) :
    if(n == 1):
       return 1

    result = 0
    k = n//2 + 1
    for i in range(2, k) :
        if (n % i == 0) :
                result = result + (i)
    return (result+1)
   
n = 30
print(divSum(n))