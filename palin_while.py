# Adapted from https://www.w3resource.com/java-exercises/recursive/java-recursive-exercise-4.php

def isPalindrome(str) :
    strLength = len(str)
    return isPalindromeHelper(str, 0, strLength - 1)

def isPalindromeHelper(str, first, last) :
    while (last - first) > 1 :

        firstChar = str[first:first + 1]
        lastChar = str[last:last + 1]

        if firstChar != lastChar :
            return False

        first += 1
        last -= 1

    # the remaining string is either 1 char or empty and all previous checks passed
    return True

palindrome1 = "madam"
isPalindrome1 = isPalindrome(palindrome1)
print(palindrome1 + " is a palindrome: " + str(isPalindrome1))

palindrome2 = "levvel"
isPalindrome2 = isPalindrome(palindrome2)
print(palindrome2 + " is a palindrome: " + str(isPalindrome2))

notPalindrome = "python"
isPalindrome3 = isPalindrome(notPalindrome)
print(notPalindrome + " is a palindrome: " + str(isPalindrome3))
