import string
def find_longest_word(sentence):
    translator = str.maketrans('', '', string.punctuation)
    clean_sentence = sentence.translate(translator)
    words = clean_sentence.split()
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word
user_sentence = input("Enter a sentence: ")
longest = find_longest_word(user_sentence)
print("The longest word is:", longest)