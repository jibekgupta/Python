def search(num,target):
    l,r=0,len(num)-1

    while l<=r:
        m=l+((r-1)//2)
        if num[m] >target:
            r=m-1
        elif num[m]<target:
            l=m+1
        else:
            return m
    return -1

num1=[-1,0,3,5,9,12]        #output:4
target1=9
num2=[-1,0,3,5,9,12]        #output:-1
target2=2
print(search(num1,target1))
print(search(num2,target2))