#author:RED 12/7/22


word= 'AbracadabrA'
i=0
count=0
words= word.lower()
while i< len(words):
    if words[i]=='a':
        count+=1
    i+=1
print(count)
