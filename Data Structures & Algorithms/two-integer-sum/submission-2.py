class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            r = target - x
            if r in hashmap:
                return [hashmap[r], i]
            hashmap[x] = i