num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = int(input("Enter any (1-add, 2-sub,3-mul,4-div) "))

result = 0
if ch == 1:
    result = num1 + num2
elif ch == 2:
    result = num1 - num2
elif ch == 3:
    result = num1 * num2
elif ch == 4:
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(result)