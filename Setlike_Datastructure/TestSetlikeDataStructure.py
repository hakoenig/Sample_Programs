import unittest
import collections
from SetlikeDataStructure import SetlikeDataStructure


class TestLongestSubstring(unittest.TestCase):

    def test_correct_working(self):
        """
        Checking if data structure is truly setlike (only one "a" and one (1, 2) should be part
        of the data_structure) and if GetRandomElement returns valid element.
        """
        self.assertTrue(collections.Counter(data_structure.GetAllElements()) == collections.Counter([1, 2, "a", "A", "", (1, 2)]))
        self.assertTrue(data_structure.GetRandomElement() in [1, 2, "a", "A", "", "RGB", (1, 2)])
        
    def test_randomness_of_GetRandomElement(self):
        """
        Checking if GetRandomElement returns elements randomly, i.e., if more than
        one element gets selected.
        """
        list_of_random_values = []
        for i in range(50):
            list_of_random_values.append(data_structure.GetRandomElement())
        
        self.assertTrue(len(set(list_of_random_values)) > 1)
    
    def test_mutable_input(self):
        """
        Mutable inputs cannot be used and should trigger a ValueError.
        """
        with self.assertRaises(ValueError):
            data_structure.Insert(["1", "2"])

if __name__ == "__main__":
    
    data_structure = SetlikeDataStructure()
    list_of_elements = [1, 2, "a", "a", "A", "", "RGB", (1, 2), (1, 2)]
    for elem in list_of_elements:
        data_structure.Insert(elem)
    
    data_structure.Remove("RGB")

    unittest.main(exit = False)
