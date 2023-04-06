
def pairStar(Input, Output, i = 0) :
     
    Output = Output + Input[i]
 
    if (i == len(Input) - 1) :
        print(Output)
        return;
 
    if (Input[i] == Input[i + 1]) :
        Output = Output + '*';
 
    pairStar(Input, Output, i + 1);
 

 
Input = input()
Output = ""
pairStar(Input, Output)