from typing import List

"""
My solution
Time: O(NlogN) due to sorting array at the end 
Space: O(N) where we built a hash map for wins and losses
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, loss = {}, {}

        for v in matches:
            if v[0] in win:
                win[v[0]] += 1
            elif v[0] not in win:
                win[v[0]] = 1
            if v[1] in loss:
                loss[v[1]] += 1
            elif v[1] not in loss:
                loss[v[1]] = 1

        res1, res2 = [], []

        for l in loss:
            if loss[l] == 1:
                res2.append(l)

        for w in win:
            if w not in loss:
                res1.append(w)

        return [sorted(res1), sorted(res2)]


"""
LeetCode Solution
Time: O(n + k) for each match, iterate over O(n) for each
player which takes O(k) time

Space: O(k) need to create an array of size O(k) to cover
all players
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1

        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer
