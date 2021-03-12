import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re
from textblob import TextBlob
from config import STOPWORDS

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')



def stemmer(text_list):
    new_text_list = []
    ps = PorterStemmer()

    for text in text_list:
        stemmed_text = ps.stem(text)
        new_text_list.append(stemmed_text)
        if text != stemmed_text:
            #print(text + "->" + stemmed_text)
            pass
    return new_text_list


def lemmatize(text_list):
    new_text_list = []
    lemmatizer = WordNetLemmatizer()
    for text in text_list:
        lemmed_text = lemmatizer.lemmatize(text)
        new_text_list.append(lemmed_text)
        if text != lemmed_text:
            # print(text + "->" + lemmed_text)
            pass

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
