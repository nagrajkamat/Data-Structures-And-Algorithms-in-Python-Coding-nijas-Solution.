from sys import stdin
def tripletSum(arr, n, num) :
    arr.sort()
    count=0
    for i in range(n-2):
        l=i+1
        r=n-1
        while l<r:
            n_l=1
            n_r=1
            temp=arr[i]+arr[l]+arr[r]
            if temp==num:
                while l<r and arr[l+1]==arr[l]:
                    l+=1
                    n_l+=1
                while l<r and arr[r-1]==arr[r]:
                    r-=1
                    n_r+=1
                if l==r:
                    count+=(n_l*(n_l-1))//2
                else:
                    count+=n_l*n_r
                l+=1
                r-=1
            elif temp>num:
                r-=1
            else:
                l+=1
    return count



#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1