from preprocess import clean_text
import math


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
        self.word_dict[word] / len(self.word_dict)

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
        return math.acos(dot_product / (abs_first * abs_second))

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
        total_document = len(self.books)
        docs_with_term = len([book for book in self.books if word in book.word_dict])
        return math.log(total_document / docs_with_term)

    def matching_score(self, query_book):
        m_scores = [{'book': book, 'score': 0} for book in self.books]

        for word in query_book.word_dict:
            for i, book in enumerate(self.books):
                if word in book.word_dict:
                    m_scores[i]['score'] += book.tfidf[word]
        m_scores = sorted(m_scores, key=lambda x: x['score'], reverse=True)
        return m_scores

    def get_total_vocab(self):
        total_vocab = []
        for book in self.books:
            total_vocab += list(book.keys())

        return total_vocab

    def recommend_book(self, query_book):
        self.calc_tfidf()
        m_scores = self.matching_score(query_book)
        print(m_scores)
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

        recommended_book = sorted_angles[0]
        print(recommended_book['book'].title, recommended_book['angle'])

        return {
            'matching_score': 'hejhej',
            'cosinus_similarity': 'othertitle'
        }


if __name__ == '__main__':

    my_book = Book('bunny', ['this', 'is', 'very', 'funny', 'funny'])
    print(my_book.word_count)

    BookHandler.add()

    BookHandler.recommend_book(Book())
    BookHandler.calc_tfidf()



