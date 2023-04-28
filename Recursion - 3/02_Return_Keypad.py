options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def keypad(n):
    if n==0:
        output = [""]
        return output
    smallOutput = keypad(n//10)
    currDArray = options[n%10]
    output = []
    for d in currDArray:
        for s in smallOutput:
            output.append(s+d)
    return output

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
