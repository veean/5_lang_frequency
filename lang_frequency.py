import os
import re
import collections


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        imported_text = file_handler.read()
        return imported_text


def get_most_frequent_words(text):
    text_file = re.sub('[^0-9a-zA-Zа-яА-я]+', ' ', text)
    tokens = text_file.lower().split(' ')
    most_frequent = collections.Counter(tokens).most_common(10)
    return most_frequent


if __name__ == '__main__':
    while True:
        path_totext = input('Enter filepath for txt file : ')
        if not path_totext:
            print('Try again!')
        else:
            try:
                text_uploaded = load_data(path_totext)
                print(get_most_frequent_words(text_uploaded))
                break
            except IOError as e:
                print("Try better : {}" .format(e.args[1]))
