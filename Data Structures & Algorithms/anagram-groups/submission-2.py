class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            normalized = "".join(sorted(s))
            if normalized not in hashmap:
                hashmap[normalized] = [s]
            else:
                hashmap[normalized].append(s)
        return list(hashmap.values())