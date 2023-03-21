def powerofANumber(x,n):
    if x**n==1:
        return 1
    
    smalloutput = powerofANumber(x,n-1)
    output = x*smalloutput
    return output


a,b = input().split()
x = int(a)
n = int(b)
a=powerofANumber(x,n)
print(a)