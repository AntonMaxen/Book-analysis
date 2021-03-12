import math
from preprocess import clean_text


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


def term_frequency(term, text_dict):
    return text_dict[term] / len(text_dict)


def inverse_document_frequency(word, dict_list):
    total_documents = len(dict_list)
    docs_with_term = len([my_dict for my_dict in dict_list if word in my_dict])
    return math.log(total_documents / docs_with_term)


def get_total_vocab(books):
    total_vocab = []
    for book in books:
        total_vocab += list(book.keys())

    return list(set(total_vocab))


def vectorize_book(current_book, total_vocab):
    book_vector = []
    for word in total_vocab:
        if word in current_book:
            current_tfidf = current_book[word]
            value = current_tfidf
        else:
            value = 0

        book_vector.append(value)

    return book_vector


def cosininus_similarity(a, b):
    # dot product a * b
    dot_product = sum([a[i] * b[i] for i, _ in enumerate(a)])
    abs_a = sum([num**2 for num in a])**0.5
    abs_b = sum([num**2 for num in b])**0.5
    norm_a = [num / abs_a for num in a]
    norm_b = [num / abs_b for num in b]

    return math.acos(dot_product / (abs_a * abs_b))


def calculate_tf_idf(dict_list):
    tf_idf_dict_list = []
    for text_dict in dict_list:
        new_dict = {}
        for term in text_dict:
            tf_score = term_frequency(term, text_dict)
            # print(f"{term}: \ntf_score: {tf_score}, term count in text: {text_dict[term]}")
            idf_score = inverse_document_frequency(term, dict_list)
            tf_idf = tf_score * idf_score
            new_dict[term] = tf_idf

        tf_idf_dict_list.append(new_dict)

    return tf_idf_dict_list


def matching_score(query_list, books):
    m_scores = [0 for _ in books]
    # Clean the query as you would with the books
    for word in query_list:
        for i, book in enumerate(books):
            if word in book:
                print(book[word])
                m_scores[i] += book[word]

    return m_scores

"""
tf-idf(t,d) = tf(t,d) * log(N/df + 1))

tf = Term Frequency
idf = Inverse Document Frequency
t = Term
d = Document
N = Count of corpus
df = Document Frequency 
tf(t,d) = Count of term in document / Total number of terms in document
df(t) = occurrence of term in documents

           Number of times term t appears in document               Total number of documents
tf-idf = --------------------------------------------- * log( --------------------------------------- )
               Total number of terms in document               Number of Documents with term t in it
"""


if __name__ == '__main__':
    print(cosininus_similarity([1, 0, 1], [0, 1, 2]))