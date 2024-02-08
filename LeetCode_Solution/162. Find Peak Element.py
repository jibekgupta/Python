"""A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time."""

#code

def findPeakElement(nums):
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if m < len(nums)-1   and nums[m]< nums[m+1]:
            l=m+1
        elif m>0  and nums[m] < nums[m-1]:
            r=m-1
        else:
            break
        return m


#Case Check
nums1=[1,2,3,1]                     #output:1
nums2=[1,2,1,3,5,6,4]               #output:3
print(findPeakElement(nums1))
print(findPeakElement(nums2))