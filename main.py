from scrape import scrape_url, pickle_all_urls
from preprocess import clean_text
from algorithm import create_word_count_dict, calculate_tf_idf, matching_score
from config import RANDOM_SENTENCES, book_of_interest, URL_LIST
from config import data_set


def scrape_book():
    pickle_all_urls()
    url = 'https://www.gutenberg.org/files/25830/25830-h/25830-h.htm'
    text_list = scrape_url(url)
    print([text for text in text_list])
    word_count_dict = create_word_count_dict(text_list)
    for key, value in word_count_dict.items():
        print(f"{key}: {value}")
    # with open('word_count_dict.txt', 'w') as f:
    #     for item in text_list:
    #         f.write("%s\n" % item)


def sort_dict(sentence_list):
    dict_list = calculate_tf_idf(sentence_list)
    for book in dict_list:
        new_book = dict(sorted(book.items(), key=lambda t: t[1], reverse=True))
        """
        for key, value in new_book.items():
            print(key, value)
        """
        print('_' * 10)


def scrape_and_compare():
    list_of_texts = [scrape_url(url) for url in URL_LIST]
    list_of_texts = [clean_text(text_list) for text_list in list_of_texts]
    list_of_texts = [create_word_count_dict(text_list) for text_list in list_of_texts]
    dict_list = calculate_tf_idf(list_of_texts)
    scraped_book = scrape_url(book_of_interest)
    cleaned_book = clean_text(scraped_book)
    scores = matching_score(cleaned_book, dict_list)
    print(scores)


def main():
    sentence_list = [clean_text(sentence.split()) for sentence in RANDOM_SENTENCES]
    sentence_list = [create_word_count_dict(sentence) for sentence in sentence_list]
    dict_list = calculate_tf_idf(sentence_list)
    scores = matching_score('The swirled lollipop had issues with the pop rock candy.', dict_list)
    clean_query = clean_text(book_of_interest)
    print(scores)



if __name__ == '__main__':
    scrape_and_compare()
