
def Sum_D(N):
    if N == 0:
        return 0
    
    Smalloutput = Sum_D(N//10)
    
    Output = Smalloutput + N%10 
    return Output

N = int(input())
print(Sum_D(N))
    