"""
Is Unique: implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?

questions to ask:
1.) ascii or unicode
-> we'll assume ascii in this case
-> if it's not ascii, we need to increase storage size

it's okay to assume 256 characters. This would be the case in extended ascii

Time: O(n)
Space: O(1)
"""

import unittest


def isUnique(s: str) -> bool:
    if len(s) > 128:
        return False

    char_set = [False for _ in range(128)]
    for c in s:
        val = ord(c)
        if char_set[val]:
            return False  # we already have string
        else:
            char_set[val] = True
    return True


class Test(unittest.TestCase):
    dataT = [("abcd"), ("s4fad"), ("")]
    dataF = [("23ds2"), ("hb 627jh=j ()")]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
