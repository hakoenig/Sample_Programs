import unittest
from FindWordsInString import get_more_likely_string, find_words_slicing_from_back, find_words_slicing_from_front

class TestFindWordsInString(unittest.TestCase):

    def test_correct_answer(self):
        self.assertEqual(get_more_likely_string("thecubsfinallywintheworldseries"), "the cubs finally win the world series")

    def test_not_making_up_too_many_words_sl_from_back(self):
        #we don't want to find more words than could have been in the string.
        #Example: "belowbelow" can't lead to "below below el low ow w"
        input_string = "belowbelow"
        returned_value = find_words_slicing_from_back(input_string)
        self.assertEqual(len(returned_value) - returned_value.count(" "), len(input_string))

    def test_not_making_up_too_many_words_sl_from_front(self):
        #we don't want to find more words than could have been in the string.
        #Example: "belowbelow" can't lead to "below below el low ow w"
        input_string = "belowbelow"
        returned_value = find_words_slicing_from_front(input_string)
        self.assertEqual(len(returned_value) - returned_value.count(" "), len(input_string))

    def test_identifying_more_likely_words(self):
        #options are "deeper water is dangerous" and "deeper w at eris dangerous"
        #I find the option "deeper water is dangerous" to be more likely
        self.assertEqual(get_more_likely_string("deeperwaterisdangerous"), "deeper water is dangerous")

    def test_functioning_of_avg_frequency_param(self):
        #current implemtation finds options:
        #"deeper w at eris dangerous" and "deeper water is dangerous"
        self.assertTrue(get_more_likely_string("deeperwaterisdangerous", True) != get_more_likely_string("deeperwaterisdangerous", False))

    def test_already_separated_string(self):
        #input string is not allowed to contain spaces
        with self.assertRaises(ValueError):
            get_more_likely_string("THE HOUSE IS BLUE")

    def test_empty_string(self):
        self.assertEqual(get_more_likely_string(""), "")

    def test_indifference_capitalization(self):
        #capitalization should not matter
        self.assertEqual(get_more_likely_string("THEHOUSEISBLUE").lower(), get_more_likely_string("thehouseisblue"))

if __name__ == "__main__":
    unittest.main(exit = False)
