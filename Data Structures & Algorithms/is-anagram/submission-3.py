class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        def charCount(s: str):
            hashmap = {}
            for char in s:
                if hashmap.get(char, False):
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
            return hashmap

        # compare hashmaps
        return charCount(s) == charCount(t)

                