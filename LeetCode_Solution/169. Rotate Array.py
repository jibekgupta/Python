'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
'''
def rotate(nums,k):
    k=k % len(nums)

    l,r=0,len(nums)-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    l,r=0, k-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    l,r=k,len(nums)-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    return nums #Not needed


nums1=[1,2,3,4,5,6,7]
k1=3
nums2=[-1,-100,3,99]
k2=2
print(rotate(nums1,k1))
print(rotate(nums2,k2))
