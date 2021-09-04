list1 = [10, 20, 4, 45, 99]
list2 = [9, 20, 2, 45, 99] 

list1.sort()
list2.sort()

val1 = list1[0]
val2 = list2[0]
if (val1 - val2 < 0):
    print(val2 - val1)
else:
    print(val1 - val2)