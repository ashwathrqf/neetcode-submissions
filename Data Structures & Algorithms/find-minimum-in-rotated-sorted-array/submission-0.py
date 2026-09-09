class Solution:
    def findMin(self, nums: List[int]) -> int:
        s=0
        e=len(nums)-1
        while s<e:
            m=(s+e)//2
            if nums[m]<nums[e]:
                e=m
            else:
                s=m+1
        return nums[s]

        