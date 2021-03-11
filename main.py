from scrape import scrape_url, pickle_all_urls
from preprocess import clean_text
from algorithm import create_word_count_dict, calculate_tf_idf
from config import RANDOM_SENTENCES


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


def main():
    sentence_list = [clean_text(sentence.split()) for sentence in RANDOM_SENTENCES]
    sentence_list = [create_word_count_dict(sentence) for sentence in sentence_list]
    calculate_tf_idf(sentence_list)

    # for sentence in sentence_list:
    #     for key, value in sentence.items():
    #         print(f"{key}: {value}")
    #     print('------------------'*10)



if __name__ == '__main__':
    main()
