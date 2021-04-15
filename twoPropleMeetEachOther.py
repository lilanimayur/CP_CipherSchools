#two people meet each other
'''There are two people that start from two different positions, let’s say x1 and x2. Both can jump v1 and v2 meters ahead respectively. We have to find if both will ever meet given that the number of jumps taken by both has to be same.

Print ‘Yes’ if they will meet,
print ‘No’ they will not.'''

def jump(x1,x2,v1,v2):
    if(x1>x2 and v1>v2):
        print("No")
    if(x2>x1 and v2>v1):
        print("No")
    if(abs(x1-x2)%abs(v1-v2)==0):
        print("Yes")
    else:
        print("No")



def main():
    p1=int(input())
    p2=int(input())
    j1=int(input())
    j2=int(input())
    jump(p1,p2,j1,j2)


if __name__ == "__main__":
    main()
