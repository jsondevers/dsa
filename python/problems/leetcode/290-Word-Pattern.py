# Time: O(N) where N is max(len(pattern), len(words))
# Space: O(N), the hashmap for the characters is technically O(26) -> O(1) for letters in the alphabet, but the words array is O(N) where N is the number of words


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_dict = {}  # character -> word
        word_dict = {}  # word -> character
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            character = pattern[i]
            word = words[i]

            if character not in char_dict:
                if word in word_dict:
                    return False
                char_dict[character] = word
                word_dict[word] = character
            else:
                if character in char_dict and char_dict[character] != word:
                    return False

        return True
