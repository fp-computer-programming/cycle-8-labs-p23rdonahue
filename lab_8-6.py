#author: RED 12/7/22

num = int(input("Input a number ")) #input statement for number

def factorial(num): #making function
    i = 1
    f = 1
    while num >= i: #making loop
        f = f * i
        i += 1
    return f #return the factorial

print(factorial(num))
