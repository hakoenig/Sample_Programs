import sys
import enchant
import wikiwords


d = enchant.Dict("en_US")

def get_likelihood_of_string(string, avg_frequency = False):
    """
    Finds individual words in string of multiple words that is 
    missing spaces between words. Does so by reducing string from the back
    and checking if resulting string is a word in English dictionary.
    
    In:
        string (str): string of words separated by spaces
        avg_frequency (bool): boolean whether or not to calculate avg frequency of words 
    Out:
        sum_frequency (float): likelihood of string
    """

    sum_frequency = 0
    list_of_words = string.split(" ")
    
    for word in list_of_words:
        sum_frequency += wikiwords.freq(word.lower())
    if avg_frequency:
        sum_frequency = sum_frequency / len(list_of_words)

    return sum_frequency


def find_words_slicing_from_back(string):
    """
    Finds individual words in string of multiple words that is 
    missing spaces between words. Does so by reducing string from the back
    and checking if resulting string is a word in English dictionary.
    
    In:
        string (str): string that needs to be broken down into words
    Out:
        string with individual words separated by spaces.
    """
    if not isinstance(string, str):
        raise ValueError("Not a valid input. Expecting string as input.")
    
    list_of_words = []
    list_to_skip_is = []
    current_string = string
    
    for i in range(len(string)):
        
        is_word = False
        
        if i in list_to_skip_is:
            continue
            
        current_string = string[i:]
        
        if d.check(current_string):
            list_of_words.append(current_string)
            list_to_skip_is = [x for x in range(len("".join(list_of_words)))]
            continue
        
        while not is_word and len(current_string) > 1:
            
            current_string = current_string[:-1]
            
            if d.check(current_string):
                list_of_words.append(current_string)
                list_to_skip_is = [x for x in range(len("".join(list_of_words)))]
                is_word = True

    return " ".join(list_of_words)


def find_words_slicing_from_front(string):
    """
    Finds individual words in string of multiple words that is 
    missing spaces between words. Does so by reducing string from the front
    and checking if resulting string is a word in English dictionary.
    
    In:
        string (str): string that needs to be broken down into words
    Out:
        string with individual words separated by spaces.
    """
    if not isinstance(string, str):
        raise ValueError("Not a valid input. Expecting string as input.")
    
    list_of_words = []
    
    while(string):
        
        is_word = False
         
        current_string = string
        
        if d.check(current_string):
            list_of_words.append(current_string)
            string = string[:string.find(current_string)]
            continue
        
        while not is_word and len(current_string) > 1:
            
            current_string = current_string[1:]
            
            if d.check(current_string):
                list_of_words.append(current_string)    
                string = string[:string.rfind(current_string)]
                is_word = True

    list_of_words.reverse()
    return " ".join(list_of_words)


def get_more_likely_string(string, avg_frequency = False):
    """
    Finds individual words in string of multiple words that is 
    missing spaces between words. Leverages functions find_words_slicing_from_back
    and find_words_slicing_from_front to identify possible strings and uses wikipedia 2012 
    word counts to determine which string is more likely.
    
    In:
        string (str): string that needs to be broken down into words
        avg_frequency (bool): boolean whether or not to use avg frequency of string
                              to determine which string is more likely 
    Out:
        string with individual words separated by spaces.
    """

    if not isinstance(string, str):
        raise ValueError("Not a valid input. Expecting string as input.")
    
    if " " in string:
        raise ValueError("Not a valid input. String contains spaces. Did you already find all of the words?")
    
    if not isinstance(avg_frequency, bool):
        raise ValueError("Not a valid input. Expecting bool as input for avg_frequency.")
    
    find_words_from_back_sequence = find_words_slicing_from_back(string)
    find_words_from_front_sequence = find_words_slicing_from_front(string)

    if find_words_from_back_sequence == find_words_from_front_sequence:
        return find_words_from_back_sequence

    print("Took two approaches to find words. My options were:\n\t1: {}\t2: {}".format(find_words_from_back_sequence, find_words_from_front_sequence))
    
    sum_find_words_from_back = get_likelihood_of_string(find_words_from_back_sequence, avg_frequency)
    sum_find_words_from_front = get_likelihood_of_string(find_words_from_front_sequence)
        
    print("This string seems more likely:")
    if sum_find_words_from_front > sum_find_words_from_back:
        return find_words_from_front_sequence
    else:
        return find_words_from_back_sequence


if __name__ == "__main__":

    if len(sys.argv) == 3:
        if sys.argv[2] == "True":
            likely_string = get_more_likely_string(sys.argv[1], True)
        else:
            likely_string = get_more_likely_string(sys.argv[1], False)
    else:
        likely_string = get_more_likely_string(sys.argv[1])
    
    print(likely_string)
    







