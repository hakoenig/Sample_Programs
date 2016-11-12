import random as rn
import sys

class SetlikeDataStructure(object):
    """
    Class that represents a setlike data structure. Supported methods are:
     - Insert
     - Remove
     - GetRandomElement
     - GetAllElements
    """
    
    def __init__(self):
        """
        Initializes an instance of a setlike data structure.
        """
        self._elements = {}
    
    
    def Insert(self, element):
        """
        Adds element to data structure if it is not already part of it.
        
        Input:
            - element (immutable type): element that shall be added to the data structure.
        Output:
            - No output.
        """
        if not isinstance(element, (str, int, bool, float, tuple)):
            raise ValueError("Not a valid element. Can only insert immutable elements.")
        if element not in self._elements:
            self._elements[element] = 0
        else:
            print("This element is already included.")
    
    
    def Remove(self, element):
        """
        Removes element from data structure.
        
        Input:
            - element: element that shall be removed from data structure.
        Output:
            - No output.
        """
        if element in self._elements:
            del self._elements[element]
        else:
            print("Element was not included.")
    
    
    def GetRandomElement(self):
        """
        Returns random element from data structure.
        
        Input:
            - No input.
        Output:
            - element: random element from data structure.
        """
        if len(self._elements) > 0:
            return rn.choice(list(self._elements.keys()))
        else:
            return ""
    
    
    def GetAllElements(self):
        """
        Returns list of all elements from data structure.
        
        Input:
            - No input.
        Output:
            - list of all elements from data structure.
        """
        return list(self._elements.keys())
    
    
    def __repr__(self):
        """
        Returns a string representation of SetlikeDataStructure.
        """
        return "This is an instance of SetlikeDataStructure.\nMy elements are: {}".format(self.GetAllElements())


if __name__ == "__main__":
    data_structure = SetlikeDataStructure()
    list_of_elements = sys.argv[1].strip("[").strip("]").split(",")
    if list_of_elements:
        for elem in list_of_elements:
            data_structure.Insert(elem)
    data_structure.Remove(rn.choice(list_of_elements))
    print(data_structure.GetRandomElement())
    print(data_structure.GetAllElements())








