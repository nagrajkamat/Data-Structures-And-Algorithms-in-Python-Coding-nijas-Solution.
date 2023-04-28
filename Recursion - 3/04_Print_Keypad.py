def PrintKeypad(n,d,ans=""):
    if n==0:
        print(ans)
        return
    ch=n%10
    inp=n//10
    s=d[ch]
    for i in s:
        PrintKeypad(inp,d,i+ans)
    
n=int(input())
d=d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
PrintKeypad(n,d)
