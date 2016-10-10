import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        imported_text = file_handler.readlines()
        return imported_text

def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    pass