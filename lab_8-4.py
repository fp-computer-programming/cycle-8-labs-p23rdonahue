# author: RED 12/6/22

def sum(n): #making function
    i=0
    total = 0
    while i<(n+1): #making while loop
        total += i
        i+=1
        
    return total #return total of sum
print(sum(5))