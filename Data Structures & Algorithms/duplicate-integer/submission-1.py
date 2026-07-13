class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if hashmap.get(num, 0) > 0:
                return True
            else:
                hashmap[num] = 1
        return False