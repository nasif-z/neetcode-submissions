class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force pass
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    continue
                if x + y == target:
                    return [i, j]