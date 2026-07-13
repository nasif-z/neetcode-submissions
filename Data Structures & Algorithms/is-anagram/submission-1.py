class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def charCount(s: str):
            hashmap = {}
            for char in s:
                if hashmap.get(char, False):
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
            return hashmap

        hashmap_s = charCount(s)
        hashmap_t = charCount(t)

        # compare hashmaps
        return hashmap_s == hashmap_t

                