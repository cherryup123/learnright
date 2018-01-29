def break_words(stuff):
    """"This function will break up words for us."""
    words = stuff.split()
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poping it off."""
    word= words.pop(0)
    print word

def print_last_word(words):
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print(print_first_word(words))
    print(print_last_word(words))

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print(print_first_word(words))
    print(print_last_word(words))

# print (break_words('s a m'))
# print (sort_words('sam'))
# print (print_first_word(['a',1]))
# print (print_last_word(['a',1]))
#
# print (sort_sentence("this is a question"))
# print_first_and_last("this is a question")
# print_first_and_last_sorted("this is a question")