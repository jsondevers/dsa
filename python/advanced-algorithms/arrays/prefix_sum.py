class PrefixSum:
    # prefix: start at the beginning
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft


# pre-computed, we can get the values computed at each in O(1) time
# pre-computing work, makes additional work easier
nums = [1, 2, -1, -5, 1, 6]
prefix_sum = PrefixSum(nums)
print(prefix_sum.rangeSum(0, 5))
