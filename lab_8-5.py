#author:RED 12/7/22


word= 'AbracadabrA' #making word
i=0
count=0
words= word.lower() #making lowercase
while i< len(words): #making loop
    if words[i]=='a':
        count+=1 #adding 1 if there is an a
    i+=1
print(count) #printing
