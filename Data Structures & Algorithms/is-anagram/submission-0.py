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

        # sort both hashmap
        hashmap_s = dict(sorted(hashmap_s.items()))
        hashmap_t = dict(sorted(hashmap_t.items()))

        # compare hashmaps
        return hashmap_s == hashmap_t

                