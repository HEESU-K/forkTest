def swap(num1, num2):
    temp = num2
    num2 = num1
    num1 = temp
    return (num1, num2)
    
###############################################

num1, num2 = 10, 5

print("교환하기 전")
print(num1, num2)

print("두 수의 교환")
num1, num2 = swap(num1, num2)
print(num1, num2)