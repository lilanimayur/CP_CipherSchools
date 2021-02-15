'''You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.'''

def missingValue(arr,l):
    sum=0
    t_sum=(l+1)*(l+2)/2
    for i in range(l):
        sum=sum+arr[i]
    return abs(t_sum-sum)

n=int(input("Enter number of elements in array"))
ar=[]
for i in range(n):
    x=int(input())
    ar.append(x)
print(missingValue(ar,n))