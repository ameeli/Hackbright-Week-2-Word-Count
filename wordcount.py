import string
import sys
def word_count(file_):
    """
    Opens specified file, iterates through line then words in the file and returns 
    a dictionary with words as keys and counts as values.
    """
    with open(file_) as inputs:
        count_words = {}

        for line in inputs:
            words = line.rstrip().split(' ')

            for word in words:
                word = word.translate(None, string.punctuation).lower()
                count_words[word] = count_words.get(word, 0) + 1

        return count_words


def print_counted_words(file_):
    """
    Calls word_count() with specified file, takes the dictionary returned by word_count
    and prints out each key/value pair on a separate line.
    """
    count_words = word_count(file_)    
    for word, count in count_words.items():
        print '%s %d' % (word, count)


print_counted_words(sys.argv[1])



