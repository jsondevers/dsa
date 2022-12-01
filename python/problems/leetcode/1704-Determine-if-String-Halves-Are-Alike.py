class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        first = 0
        second = 0

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] in vowels:
                first += 1
            if s[right] in vowels:
                second += 1
            left += 1
            right -= 1
        return first == second
