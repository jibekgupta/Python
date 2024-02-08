"""An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity."""

#code
def peakIndexInMountainArray(arr):
    l,r=0,len(arr)-1

    while l<r:
        m=(l+r)//2

        if arr[m] >arr[m+1]:
            r=m
        else:
            l=m+1

    return l
#Case Check
arr1=[0,10,5,2]         #output:1
arr2=[0,2,1,0]          #output:1
arr3=[0,10,5,2]         #output:1
print(peakIndexInMountainArray(arr1))
print(peakIndexInMountainArray(arr2))
print(peakIndexInMountainArray(arr3))