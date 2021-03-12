from bs4 import BeautifulSoup
import requests
import pickle
from pathlib import Path
import path_management as pm
from preprocess import clean_text
from config import URL_LIST


def pickle_result(result):
    book_folder = pm.get_bookfolder()
    bookpath = pm.get_bookpath(result.url)
    Path(book_folder).mkdir(parents=True, exist_ok=True)
    with open(bookpath, 'wb+') as p_file:
        pickle.dump(result, p_file)

    return bookpath


def get_page(url):
    if pm.book_downloaded(url):
        fullpath = pm.get_bookpath(url)
    else:
        result = requests.get(url)
        if result.status_code == 200:
            fullpath = pickle_result(result)
        else:
            raise Exception(f'Request error code: {result.status_code}')

    return fullpath


def load_page(full_path):
    with open(full_path, 'rb') as p_file:
        unpickled_page = pickle.load(p_file)

    return BeautifulSoup(unpickled_page.text, 'html.parser')


def trim_page(soup, identifiers):
    for element in soup.find_all(*identifiers):
        element.decompose()


def filter_page(soup):
    removal = True
    for i, element in enumerate(soup.body.find_all()):
        if '*** START' in element.text:
            element.decompose()
            removal = False
        elif '*** END' in element.text:
            removal = True

        if removal:
            element.decompose()


def scrape_url(url):
    full_path = get_page(url)
    soup = load_page(full_path)
    filter_page(soup)
    text_list = soup.body.get_text(separator="\n", strip=True).split()
    text_list = clean_text(text_list)
    return text_list


def pickle_all_urls():
    for url in URL_LIST:
        full_path = get_page(url)
        soup = load_page(full_path)
