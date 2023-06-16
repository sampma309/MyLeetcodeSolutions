class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            if (target - nums[i]) in ht:
                return [i, ht[target - nums[i]]]
            else:
                ht[nums[i]] = i