# Adapted from https://www.w3resource.com/java-exercises/recursive/java-recursive-exercise-4.php

def isPalindrome(str) :
    strLength = len(str)
    if strLength <= 1 :
        return True

    firstChar = str[0:1]
    lastChar = str[-1]

    if firstChar != lastChar :
        return False

    remainingSubstring = str[1:strLength - 1]
    return isPalindrome(remainingSubstring)

palindrome1 = "madam"
isPalindrome1 = isPalindrome(palindrome1)
print(palindrome1 + " is a palindrome: " + str(isPalindrome1))

palindrome2 = "levvel"
isPalindrome2 = isPalindrome(palindrome2)
print(palindrome2 + " is a palindrome: " + str(isPalindrome2))

notPalindrome = "java"
isPalindrome3 = isPalindrome(notPalindrome)
print(notPalindrome + " is a palindrome: " + str(isPalindrome3))
