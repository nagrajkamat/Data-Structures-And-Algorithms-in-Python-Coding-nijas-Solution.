## Read input as specified in the question.
## Print output as specified in the question.
def printSubsequences(string, path) :
    
    if len(string) == 0 :
        print(path)
        return
        
    printSubsequences(string[1:], path)
    printSubsequences(string[1:], path+string[0])
    
    
#main
string = input().strip()
printSubsequences(string, '')