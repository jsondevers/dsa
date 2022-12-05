# Time: O(nlogn) because we use sort
# Space: O(n) because of building the hash map
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        sort_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
        res = []
        print(print(sort_letters))
        for k, v in sort_letters:
            while v != 0:
                res.append(k)
                v -= 1

        return "".join(res)


# Time: O(n)
"""
Like before, the HashMap building has a cost of O(n)O(n).

The bucket sorting is O(n)O(n), because inserting items has a cost of O(k)O(k) (each entry from the HashMap), and building the buckets initially has a worst case of O(n)O(n) (which occurs when k = 1k=1). Because k ≤ nk≤n, we're left with O(n)O(n).

So in total, we have O(n)O(n).

It'd be impossible to do better than this, because we need to look at each of the nn characters in the input String at least once.
"""
# Space: O(n)
def frequencySort(self, s: str) -> str:
    if not s:
        return s

    # Determine the frequency of each character.
    counts = Counter(s)
    max_freq = max(counts.values())

    # Bucket sort the characters by frequency.
    buckets = [[] for _ in range(max_freq + 1)]
    for c, i in counts.items():
        buckets[i].append(c)

    # Build up the string.
    string_builder = []
    for i in range(len(buckets) - 1, 0, -1):
        for c in buckets[i]:
            string_builder.append(c * i)

    return "".join(string_builder)
