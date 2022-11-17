"""
One Away: There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false 
"""
import unittest

# my solution
# Time: O(n), Space: O(n)
def one_away(s: str, t: str) -> bool:
    s_pair = dict()  # character -> number of characters
    t_pair = dict()

    for c in s:
        if c in s_pair:
            s_pair[c] += 1
        else:
            s_pair[c] = 1

    for c in t:
        if c in t_pair:
            t_pair[c] += 1
        else:
            t_pair[c] = 1

    count_differences = 0
    for c in s:
        if not (c in t_pair and t_pair[c] == s_pair[c]):
            count_differences += 1

    return count_differences == 1


# book's solution
# Time: O(n), Space: O(1)
def one_away(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

    class Test(unittest.TestCase):
        """Test Cases"""

        data = [
            ("pale", "ple", True),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("paleabc", "pleabc", True),
            ("pale", "ble", False),
            ("a", "b", True),
            ("", "d", True),
            ("d", "de", True),
            ("pale", "pale", True),
            ("pale", "ple", True),
            ("ple", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
            ("pale", "pse", False),
            ("ples", "pales", True),
            ("pale", "pas", False),
            ("pas", "pale", False),
            ("pale", "pkle", True),
            ("pkle", "pable", False),
            ("pal", "palks", False),
            ("palks", "pal", False),
        ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
