class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp=[0]*len(nums)
        pp[0]=1
        sp=[0]*len(nums)
        sp[len(nums)-1]=1
        for i in range(1,len(nums)):
            pp[i]=pp[i-1]*nums[i-1]
            sp[len(nums)-i-1]=sp[len(nums)-i]*nums[len(nums)-i]
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=pp[i]*sp[i]
        return res



        