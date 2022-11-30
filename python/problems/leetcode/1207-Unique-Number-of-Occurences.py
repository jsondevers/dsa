from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        pair = {}

        for i in arr:
            if i in pair:
                pair[i] += 1
            else:
                pair[i] = 1

        return len(set(pair.values())) == len(pair)
