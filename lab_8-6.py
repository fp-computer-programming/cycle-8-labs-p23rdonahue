#author: RED 12/7/22

num = int(input("Input a number "))

def factorial(num):
    i = 1
    f = 1
    while num >= i:
        f = f * i
        i += 1
    return f

print(factorial(num))
