class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tar=defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in tar:
                return [tar[target-nums[i]],i]
            tar[nums[i]]=i




        