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
    text = re.sub('[^A-zА-я]+', ' ', text)
    tokens = text.lower().split(' ')
    words_to_show = 10
    most_frequent = collections.Counter(tokens).most_common(words_to_show)
    return most_frequent


if __name__ == '__main__':
    while True:
        try:
            path_totext = input('Enter filepath for txt file : ')
            if not path_totext:
                print('Try again!')
            else:
                try:
                    text_uploaded = load_data(path_totext)
                    if text_uploaded:
                        print(get_most_frequent_words(text_uploaded))
                    break
                except FileNotFoundError as e:
                    print("Try better : {}" .format(e.args[1]))
        except KeyboardInterrupt as interrupt:
            print("Stopping if you want... - {}".format(interrupt.args[1]))

