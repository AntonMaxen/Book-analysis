import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import re
from textblob import TextBlob
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
STOPWORDS = stopwords.words('english') + ['and']


def stemmer(text_list):
    new_text_list = []
    ps = PorterStemmer()

    for text in text_list:
        stemmed_text = ps.stem(text)
        new_text_list.append(stemmed_text)
        if text != stemmed_text:
            print(text + "->" + stemmed_text)
    return new_text_list


def lemmatize(text_list):
    new_text_list = []
    lemmatizer = WordNetLemmatizer()
    for text in text_list:
        lemmed_text = lemmatizer.lemmatize(text)
        new_text_list.append(lemmed_text)
        if text != lemmed_text:
            print(text + "->" + lemmed_text)

    return new_text_list


def remove_encoding(text_list):
    text_list = [text.encode('ascii', 'ignore').decode() for text in text_list]
    return text_list


def remove_symbols(text_list):  # TODO: maybe exculde apostrophes and make separate method?
    text_list = [re.sub('[^a-zA-Z0-9 ]', '', text) for text in text_list]
    return text_list


def remove_singel_characters(text_list):
    return [text for text in text_list if len(text) > 1]


def remove_empty_strings(text_list):
    return [text for text in text_list if text]


def text_list_to_lower(text_list):
    return [text.lower() for text in text_list]


def remove_stop_words(text_list):
    return [term for term in text_list if term not in STOPWORDS]


def create_word_count_dict(text_list):
    term_dict = {}
    for term in set(text_list):
        term_dict[term] = count_term_in_text(term, text_list)
    sorted_term_dict = sort_dictionary(term_dict)
    return sorted_term_dict


def count_term_in_text(term, text_list):
    tf = 0
    for text in text_list:
        if term == text:
            tf += 1
    return tf


def sort_dictionary(unsorted_dict):
    sorted_dict = {}
    sorted_keys = sorted(unsorted_dict, key=unsorted_dict.get)
    for key in sorted_keys:
        sorted_dict[key] = unsorted_dict[key]
    return sorted_dict


def remove_duplicate_terms(text_list):
    unique_terms = []
    for term in text_list:
        if term not in unique_terms:
            unique_terms.append(term)
    return unique_terms


def clean_text(text_list):
    text_list = remove_encoding(text_list)
    text_list = text_list_to_lower(text_list)
    text_list = remove_stop_words(text_list)
    text_list = remove_symbols(text_list)
    text_list = remove_singel_characters(text_list)
    text_list = remove_empty_strings(text_list)
    text_list = lemmatize(text_list)
    text_list = stemmer(text_list)
    return text_list
