## Print output as specified in the question.
def subset(arr):
    n=len(arr)
    if(n<=0):
        output = [ [] ]
        return output

    output = subset(arr[:n-1])
    outputLen = len(output)
    #output *= 2 This copies the reference. We need shallow copies
    for i in range(0, outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(arr[n-1])
    return output

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
output=subset(arr)
for lst in output:
    for num in lst:
        print(num, end=' ')
    print()