"""
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. 

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)

questions to ask:
1.) does capitalization matter?
2.) if we get a phrase, do we have to worry about non-alphabetical characters?

A palindrome is a string that is the same forwards and backwards. 
Therefore, to decide if a string is a permutation of a palindrome, 
we need to know if it can be written such that it's the same forwards and backwards.

What does it take to be able to write a set of characters the same way forwards 
and backwards? We need to have an even number of almost all characters, 
so that half can be on one side and half can be on the other side. 
At most one character (the middle character) can have an odd count. 
For example, we know tactcoapapa is a permutation of a palindrome 
because it has 
two Ts, four As, two Cs, two Ps, and one 0. 
That O would be the center of all possible palindromes.
"""

"""
Note that none of these solutions created all possible permutations,
then checked if they were palindromes. Creating all possible permutations 
in the real world would take factorial time (which is really bad).
"""
import unittest

# Solution 1: Hash Table
# Time: O(N), Space: O(N) for the hash-table
# Implementing this algorithm is fairly straightforward.
# We use a hash table to count how many times each character appears.
# Then, we iterate through the hash table and ensure that no more
# than one character has an odd count.

# Solution 2: Check number of odds as you go
# Time: O(n), Space: O(1)
def palindromic_subtring(s: str) -> bool:
    countOdd = 0
    table = [0 for _ in range((ord("z") - ord("a")) + 1)]
    for c in s:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                countOdd += 1
            else:
                countOdd -= 1
    return countOdd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


# Solution 3: Bit-Masking (look at book)


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindromic_subtring(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
