'''Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. 
A majority element in an array A[] of size n is an element that appears more than n/2 times 
(and hence there is at most one such element). '''

def majorityElement(arr, size):
    arr.sort()
    temp=arr[0]
    count=-1
    t_count=1
    check=1
    for i in range(1,size):
        if(temp==arr[i]):
            t_count+=1
        else:
            temp=arr[i]
            t_count=1

        if count<t_count:
            count=t_count
            mE=arr[i]

            if count>size//2:
                check=1
                break
    if check==1:
        print(mE)
    else:
        print("No Majority Element")



def main():
    s=int(input("Enter size of arry "))
    l=[]
    for i in range(s):
        a=int(input())
        l.append(a)
    majorityElement(l,s)

if __name__ == "__main__":
    main()