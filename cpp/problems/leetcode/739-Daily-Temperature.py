from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # track the indexes
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                s_index = stack.pop()
                res[s_index] = (
                    i - s_index
                )  # number of days it takes to have greater temp
            stack.append(i)
        return res
