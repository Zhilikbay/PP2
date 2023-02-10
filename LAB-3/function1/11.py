def is_palindrome(word):
    
    word = word.replace(" ", "").lower()
    
    rev_word = word[::-1]
    
    if word == rev_word:
        return True
    else:
        return False

print(is_palindrome("Madam")) 
print(is_palindrome("Palindrome")) 