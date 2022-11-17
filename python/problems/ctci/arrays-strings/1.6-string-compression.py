"""
Implement a method to perform basic s compression using the counts
of repeated characters. For example, the s aabcccccaaa would become a2blc5a3. 
If the "compressed" s would not become smaller than the original s, 
your method should return the original s. 
You can assume the s has only uppercase and lowercase letters (a - z). 

run-length encoding
"""
import unittest


def string_compression(s: str) -> str:
    compressed = []
    counter = 0

    for i in range(len(s)):
        # s[i] and s[i - 1] are supposed to be diff characters
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(s[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(s[-1] + str(counter))

    # returns original s if compressed s isn't smaller
    return min(s, "".join(compressed), key=len)


class Test(unittest.TestCase):
    """Test Cases"""

    data = [("aabcccccaaa", "a2b1c5a3"), ("abcdef", "abcdef")]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
