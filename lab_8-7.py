#author:RED 12/8/22
def is_palindrome(word): # making function
    i=0
    while i<=len(word): # making loop so tbhat i only goes up until the length of word
        if word.lower() == word.lower()[::-1]: # making sure the lowercase and if they eqaul each other forwards and backwards
            i+=1
            return True
        else:
            i+=1
            return False

        
print(is_palindrome("SAW")) #test



