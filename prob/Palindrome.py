def isPalindrome(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

s = raw_input("Enter string: ")
print(isPalindrome(s))