import unittest
from longest_substring_of_2_chars import get_longest_substring_of_2_chars

class TestLongestSubstring(unittest.TestCase):

    def test_correct_working(self):
        self.assertEqual(get_longest_substring_of_2_chars("looooong string"), "looooo")
        self.assertEqual(get_longest_substring_of_2_chars("abbccccc"), "bbccccc")
        self.assertEqual(get_longest_substring_of_2_chars("abcdef"), "ab")

    def test_empty_string(self):
        self.assertEqual(get_longest_substring_of_2_chars(""), "")
    
    def test_string_of_one_char(self):
        self.assertEqual(get_longest_substring_of_2_chars("aaa"), "aaa")
    
    def test_different_capitalization(self):
        self.assertEqual(get_longest_substring_of_2_chars("Aaadd"), "aaadd")
    
    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            get_longest_substring_of_2_chars(1)

if __name__ == "__main__":
    unittest.main(exit = False)
