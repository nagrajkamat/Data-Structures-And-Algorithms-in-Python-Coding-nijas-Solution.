def removeX(string):
    x = 'x'
    if len(string)==0:
        return string
    
    if string[0]==x:
        return removeX(string[1:])
    else:
        return string[0] + removeX(string[1:])   

# Main
string = input()
print(removeX(string))