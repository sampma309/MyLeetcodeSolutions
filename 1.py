class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            if (target - nums[i]) in ht:
                return [i, ht[target - nums[i]]]
            else:
                ht[nums[i]] = i

""" 
Explanation:

- Create a hash table that will be used to hold the values in the array along
with their corresponding indices.
- Iterate over the array and add each value and its index into the hash table
as a key-value pair
- If the difference between the target value and the current value has already 
been seen, return its index along with the current index

Time complexity: O(N)
Space complexity: O(N)

"""