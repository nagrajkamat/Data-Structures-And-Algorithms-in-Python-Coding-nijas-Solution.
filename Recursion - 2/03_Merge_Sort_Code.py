def merge(li_1,li_2,li):
    i=0
    j=0
    k=0
    while(i< len(li_1) and j<len(li_2)):
        if(li_1[i]<li_2[j]):
            li[k]=li_1[i]
            i=i+1
            k=k+1
        else:
            li[k]=li_2[j]
            j=j+1
            k=k+1
    while(i<len(li_1)):
        li[k]=li_1[i]
        i=i+1
        k=k+1
    while(j<len(li_2)):
        li[k]=li_2[j]
        j=j+1
        k=k+1
    return li    
        
            

def merge_sort(li):
    if(len(li)==0 or len(li)==1):
        return li
    else:
        mid=len(li)//2
        li_1=li[0:mid]
        li_2=li[mid:]
        merge_sort(li_1)
        merge_sort(li_2)
        return merge(li_1,li_2,li)



n=int(input())
li=[]
li=[int(x) for x in input().split()]
x=merge_sort(li)
for i in range(0,len(x),1):
    print(x[i],end=" ")