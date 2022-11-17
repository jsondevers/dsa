"""
Assume you have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of 
s1 using only one call to isSubstring 
(e.g., "waterbottle" is a rotation of"erbottlewat"). 
"""
# O(N)
import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
