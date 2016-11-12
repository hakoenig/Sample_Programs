
## Given a string, returning the longest substring that contains at most 2 distinct characters.
## Example, for:
## "ababcbcbaaabbdef"
## we expect substring "baaabb"

import sys

def get_longest_substring_of_2_chars(string):
    """
    Returns longest substring that contains at most 2 distinct characters of a string.
    Capitalization is ignored.
    
    Input:
        string (str) - a string that the longest substring shall be found for.
        
    Output:
        longest_string (str) - longest substring of string
    """
    
    if not isinstance(string, str):
        raise ValueError("Not a valid input. Expecting string as input.")
        
    string = string.lower()
    string_length = len(string)
    longest_string = ""
    
    #iterating over input string to find all starting points 
    for i in range(string_length):
        
        start_char = string[i]
        current_longest_string = start_char
        char_list = [start_char]
        
        #iterating over input string, but starting after current start_char
        for next_char in string[i + 1:]:
            
            if next_char not in char_list:
                char_list.append(next_char)
                
            #as long as we have not seen more than 2 distinct chars, we can
            #add to the string
            if len(char_list) <= 2:
                current_longest_string += next_char
            
            else:
                if len(current_longest_string) > len(longest_string):
                    longest_string = current_longest_string
        
        # could be the case that a string only consists of one char
        # we need to check string length after loop as well
        if len(current_longest_string) > len(longest_string):
            longest_string = current_longest_string
        
    return longest_string


if __name__ == "__main__":
    longest_substring = get_longest_substring_of_2_chars(sys.argv[1])
    print(longest_substring)


