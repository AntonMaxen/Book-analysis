import nltk
from nltk.stem import WordNetLemmatizer
import re
nltk.download('wordnet')


def lemmatize(text_list):
    lemmatizer = WordNetLemmatizer()
    new_text_list = []
    for text in text_list:
        new_text_list.append(lemmatizer.lemmatize(text))

    return new_text_list


def remove_encoding(text_list):
    text_list = [text.encode('ascii', 'ignore').decode() for text in text_list]
    return text_list


def remove_symbols(text_list):
    text_list = [re.sub('[^a-zA-Z0-9 ]', '', text) for text in text_list]
    return text_list


def remove_singel_characters(text_list):
    return [text for text in text_list if len(text) > 1]


def remove_empty_strings(text_list):
    return [text for text in text_list if text]


def text_list_to_lower(text_list):
    return [text.lower() for text in text_list]


def clean_text(text_list):
    text_list = remove_encoding(text_list)
    text_list = lemmatize(text_list)
    text_list = remove_symbols(text_list)
    text_list = remove_singel_characters(text_list)
    text_list = remove_empty_strings(text_list)
    text_list = text_list_to_lower(text_list)
    return text_list
