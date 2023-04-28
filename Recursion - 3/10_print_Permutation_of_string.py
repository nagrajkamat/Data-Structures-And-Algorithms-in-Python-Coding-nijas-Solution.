def printPermutationsHelper(string,output):
    if len(string) == 0:
        print(output)
        return
    
    for i in range(len(string)):
        printPermutationsHelper(string[:i] + string[i+1:] , output + string[i])
        
def printPermutations(string):
    printPermutationsHelper(string,"")

string = input()
printPermutations(string)
