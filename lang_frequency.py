import os
import re
import collections
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        imported_text = file_handler.read()
        return imported_text


def get_most_frequent_words(text):
    text = re.sub('[^A-zА-я]+', ' ', text)
    text = text.lower().split(' ')
    words_to_show = 10
    most_frequent = collections.Counter(text).most_common(words_to_show)
    return most_frequent


if __name__ == '__main__':
    if not sys.argv[1]:
        print('Try again!')
    else:
        path_to_text = sys.argv[1]
        try:
            text_uploaded = load_data(path_to_text)
            if text_uploaded:
                for element in get_most_frequent_words(text_uploaded):
                    print('Word "{}" meets {} times '.format(element[0], element[1]))
        except FileNotFoundError as e:
            print("Try better : {}" .format(e.args[1]))
