
def word_count(file):
    """
    Opens specified file, iterates through line then words in the file and returns 
    a dictionary with words as keys and counts as values.
    """
    with open(file) as inputs:
        count_words = {}

        for line in inputs:
            words = line.rstrip().split(' ')

            for word in words:
                count_words[word] = count_words.get(word, 0) + 1

        return count_words


def print_counted_words(file):
    """
    Calls word_count() with specified file, takes the dictionary returned by word_count
    and prints out each key/value pair on a separate line.
    """
    count_words = word_count(file)    
    for word, count in count_words.items():
        print '%s %d' % (word, count)


print_counted_words('twain.txt')



