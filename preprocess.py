import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re
from textblob import TextBlob
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


def pos_tagger(text_list):
    conv_list = ' '.join(text_list)
    sent = TextBlob(conv_list)
    tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'}
    words_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemma_list = [wd.lemmatize(tag) for wd, tag in words_tags]
    # print(words_tags)
    return lemma_list


def stemmer(text_list):
    new_text_list = []
    ps = PorterStemmer()
    for text in text_list:
        new_text_list.append(ps.stem(text))
        # print(text + "->" + ps.stem(text))
    return new_text_list


def lemmatize(text_list):

    new_text_list = []
    lemmatizer = WordNetLemmatizer()
    for text in text_list:
        new_text_list.append(lemmatizer.lemmatize(text))
        # print(text + "->" + lemmatizer.lemmatize(text))
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


def clean_text(text_list):
    text_list = remove_encoding(text_list)
    text_list = text_list_to_lower(text_list)
    text_list = remove_symbols(text_list)
    text_list = remove_singel_characters(text_list)
    text_list = remove_empty_strings(text_list)
    text_list = pos_tagger(text_list)
    text_list = lemmatize(text_list)
    text_list = stemmer(text_list)
    return text_list
