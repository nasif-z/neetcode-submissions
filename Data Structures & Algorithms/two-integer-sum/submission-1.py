class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for j, x in enumerate(nums):
            r = target - x
            if hashmap.get(r) is not None:
                i = hashmap.get(r)
                return [i, j]
            else:
                hashmap[x] = j