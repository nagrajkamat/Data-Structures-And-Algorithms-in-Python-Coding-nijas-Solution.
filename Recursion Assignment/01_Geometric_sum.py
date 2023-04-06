def cv(s):
    if len(s) == 1:
        return (ord(s)-48)
    cv(s[1:])
    return int(s)

s = str(input())
print(cv(s))
