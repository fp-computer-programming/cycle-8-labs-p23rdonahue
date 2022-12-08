#author:RED 12/8/22
def is_palindrome(word):
    i=0
    while i<=len(word):
        if word.lower() == word.lower()[::-1]:
            i+=1
            return True
        else:
            i+=1
            return False

        
print(is_palindrome("SAW"))



