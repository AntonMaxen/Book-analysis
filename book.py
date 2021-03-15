from preprocess import clean_text
from scrape import scrape_url
from config import URL_LIST, book_of_interest
import math
import random


class Book:
    def __init__(self, title, text_list):
        self.title = title
        self.text = text_list
        self.clean()
        self.word_dict = self._word_count()
        self.tfidf = None
        self.vector = None

    def clean(self):
        self.text = clean_text(self.text)

    def calc_tf(self, word):
        return self.word_dict[word] / len(self.text)

    def vectorize(self, vocab):
        vector = []
        for word in vocab:
            if word in self.tfidf:
                value = self.tfidf[word]
            else:
                value = 0

            vector.append(value)

        self.vector = vector

    def cosinus_similarity(self, other_book):
        dot_product = sum([self.vector[i] * other_book.vector[i] for i, _ in enumerate(self.vector)])
        abs_first = sum([num**2 for num in self.vector])**0.5
        abs_second = sum([num**2 for num in other_book.vector])**0.5
        cos_angle = dot_product / (abs_first * abs_second)
        cos_angle = 1 if cos_angle > 1 else cos_angle
        return math.acos(cos_angle)

    def _word_count(self):
        term_dict = {}
        for term in self.text:
            if term in term_dict:
                term_dict[term] += 1
            else:
                term_dict[term] = 1

        return term_dict


class BookHandler:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, book):
        self.books.remove(book)

    def calc_tfidf(self):
        for book in self.books:
            tf_idf_dict = {}
            for term in book.word_dict:
                tf_score = book.calc_tf(term)
                idf_score = self.calc_idf(term)
                tf_idf = tf_score * idf_score
                tf_idf_dict[term] = tf_idf

            book.tfidf = tf_idf_dict

    def calc_idf(self, word):
        total_documents = len(self.books)
        docs_with_term = len([book for book in self.books if word in book.word_dict])
        return math.log((total_documents) / (docs_with_term))

    def matching_score(self, query_book):
        m_scores = [{'book': b, 'score': 0} for b in self.books]

        for word in query_book.word_dict:
            for i, book in enumerate(self.books):
                if word in book.word_dict:
                    m_scores[i]['score'] += book.tfidf[word]

        m_scores = sorted(m_scores, key=lambda x: x['score'], reverse=True)
        return m_scores

    def get_total_vocab(self):
        total_vocab = []
        for book in self.books:
            total_vocab += list(book.word_dict.keys())

        return total_vocab

    def recommend_book(self, query_book):
        self.calc_tfidf()
        m_scores = self.matching_score(query_book)
        self.add(query_book)
        self.calc_tfidf()
        vocab = self.get_total_vocab()
        query_book.vectorize(vocab)
        self.remove(query_book)

        angles = []

        for book in self.books:
            book.vectorize(vocab)
            angle = book.cosinus_similarity(query_book)
            angles.append({'angle': angle, 'book': book})

        sorted_angles = sorted(angles, key=lambda x: x['angle'])
        return {
            'matching_score': m_scores,
            'cosinus_similarity': sorted_angles
        }


def main():
    book_handler = BookHandler()
    # query_book_index = 6
    # query_book_url = URL_LIST[query_book_index]
    query_book_url = random.choice(URL_LIST)
    URL_LIST.remove(query_book_url)
    for url in URL_LIST:
        book_dict = scrape_url(url)
        book = Book(book_dict['title'], book_dict['text_list'])
        book_handler.add(book)

    query_book_dict = scrape_url(query_book_url)
    query_book = Book(query_book_dict['title'], query_book_dict['text_list'])
    result = book_handler.recommend_book(query_book)
    print('Querybook')
    print(f'Title: {query_book.title}')
    print('-' * 30)
    print('Compared books')
    print('\n'.join([f'Title: {book.title}' for book in book_handler.books]))
    print('-' * 30)
    print(f'The recommended books for ({query_book.title}) are:')
    matching_score = result['matching_score']
    cosinus_similarity = result['cosinus_similarity']

    print('By Matching Score:')
    for i, score in enumerate(matching_score):
        book = score['book']
        score = score['score']
        print(f'{i+1}: {book.title}, ({score})')

    print('-' * 30)
    print('By Cosine Similarity:')
    for i, angle in enumerate(cosinus_similarity):
        book = angle['book']
        angle = angle['angle']
        print(f'{i+1}: {book.title}, ({math.degrees(angle)})')


if __name__ == '__main__':
    main()




