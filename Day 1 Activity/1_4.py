import sys
 
def findLCM(a, b):
 
    lar = max(a, b)
    small = min(a, b)
    i = lar
    while(1) :
        if (i % small == 0):
            return i
        i += lar
     

a = 5
b = 7
print(findLCM(a, b))