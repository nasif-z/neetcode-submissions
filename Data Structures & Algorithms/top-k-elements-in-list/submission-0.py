class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_hashmap.keys())[:k]