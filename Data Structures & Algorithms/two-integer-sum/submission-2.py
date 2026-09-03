from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tar=defaultdict(int)
        seen=set()
        for i in range(len(nums)):
            if target-nums[i] in seen:
                return [tar[target-nums[i]],i]
            seen.add(nums[i])
            tar[nums[i]]=i




        