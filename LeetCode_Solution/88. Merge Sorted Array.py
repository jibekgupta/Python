'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2'''

def merge(nums1,nums2,m,n):

    last=m+n-1
    while m>0 and n>0:
        if nums1[m-1]> nums2[n-1]:
            nums1[last]= nums1[m-1]
            m-=1
        else:
            nums1[last]=nums2[n-1]
            n-=1
        last-=1

    while n> 0:
        nums1[last] =nums2[n-1]
        n,last=n-1,last-1
    
    return nums1








#Check Case
nums11 = [1,2,3,0,0,0]
m1= 3
nums21 = [2,5,6]
n1 = 3
nums12 = [1]
m2= 1
nums22 = []
n2= 0
nums13= [0]
m3 = 0
nums23 = [1]
n3 = 1
print(merge(nums11,nums21,m1,n1))           #OUTPUT: [1, 2, 2, 3, 5, 6]
print(merge(nums12,nums22,m2,n2))           #OUTPUT: [1]
print(merge(nums13,nums23,m3,n3))           #OUTPUT: [1]