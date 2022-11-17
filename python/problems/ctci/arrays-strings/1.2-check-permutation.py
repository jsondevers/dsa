"""
Check Permutation: Given two strings, write a method to decide if one is a 
permutation of the other.

questions to ask:
1.) is it case sensitive ?
is God a permutation of dog?
2.) is a white space is signifcant?
is "god    " different from "dog" 


Strings of different lengths cannot be permutations of each other.

solution 1: sort the strings
sorting takes O(nlogn)

if two strings are permutations, we know they have the same characters, 
but in different order. if we sort it, we can compare the sorted versions
"""
import unittest
from collections import Counter


def check_permutation1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_sorted = list(s)
    t_sorted = list(t)
    s_sorted.sort()
    t_sorted.sort()
    return s_sorted == t_sorted


"""
definition of permutation: two words with the same character counts
we iterate through and count how many characters are in each, then compare the 
two arrays 
"""


def check_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


class Test(unittest.TestCase):
    dataT = (
        ("abcd", "bacd"),
        ("3563476", "7334566"),
        ("wef34f", "wffe34"),
    )
    dataF = (
        ("abcd", "d2cba"),
        ("2354", "1234"),
        ("dcw4f", "dcw5f"),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation1(*test_strings)
            self.assertTrue(result)
            result = check_permutation2(*test_strings)
        # false check
        for test_strings in self.dataF:
            result = check_permutation1(*test_strings)
            self.assertFalse(result)
            result = check_permutation2(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
