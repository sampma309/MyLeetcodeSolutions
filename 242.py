class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for c in s:
            if c not in counter:
                counter[c] = [1, 0]
            else:
                counter[c][0] += 1

        for c in t:
            if c not in counter:
                return False
            else:
                counter[c][1] += 1

        for key in counter.keys():
            if counter[key][0] != counter[key][1]:
                return False
        return True

"""
Here I used a single dictionary to store the count of each letter in both s and
t as a [a, b] pair. If a != b, then s and t are not valid anagrams, otherwise
they are.

Time complexity: O(N)
Space complexity: O(1)
"""