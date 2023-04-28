def uniqueChar(s): 
    ans = '' 
    d = {} 
    for char in s: 
        if char not in d: 
            ans = ans + char 
            d[char] = True 
    return ans 
    






# Main 
s=input() 
print(uniqueChar(s))