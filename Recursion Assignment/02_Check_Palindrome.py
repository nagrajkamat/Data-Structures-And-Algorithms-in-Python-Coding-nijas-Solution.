     
def palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return 'true'
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return 'false'

s =input()
print(palindrome(s))