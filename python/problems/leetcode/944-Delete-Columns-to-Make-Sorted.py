from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for row in range(len(strs)):
                if row + 1 < len(strs) and strs[row + 1][col] < strs[row][col]:
                    count += 1
                    break
        return count
