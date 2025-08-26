#Task_5:
from collections import Counter
import string
import os
file_name = "sample.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, file_name)
def most_frequent_word(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            translator = str.maketrans('', '', string.punctuation)
            clean_text = text.translate(translator).lower()
            words = clean_text.split()
            word_counts = Counter(words)
            most_common_word, frequency = word_counts.most_common(1)[0]
            return most_common_word, frequency
    except FileNotFoundError:
        return None, 0
word, freq = most_frequent_word(file_path)
if word:
    print(f"The most frequent word is '{word}' appearing {freq} times.")
else:
    print(f"File '{file_name}' not found in the script folder.")