'''Given an array of integers, print the array in such a way that the 
first element is first maximum and second element is first minimum and so on.'''

def alternativeSorting(arr,l):
    arr.sort()
    i=0
    j=l-1
    lis=[]
    while(i<j):
        lis.append(arr[j])
        j-=1
        lis.append(arr[i])
        i+=1
    if l%2!=0:
        lis.append(arr[i])
    return lis



def main():
    n=int(input("Enter size of array"))
    ar=[]
    for i in range(n):
        x=int(input())
        ar.append(x)
    result= alternativeSorting(ar,n)
    print(result)

if __name__=='__main__':
    main()
