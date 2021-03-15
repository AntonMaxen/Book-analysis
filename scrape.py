from bs4 import BeautifulSoup
import requests
import pickle
from pathlib import Path
import path_management as pm
from config import URL_LIST
import re


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


def get_title(soup):
    paragraphs = soup.body.find_all()
    for p in paragraphs:
        if '*** START' in p.text:
            title = p.text
            title = title.strip()
            title = title.encode('ascii', 'ignore').decode()
            title = re.sub('\r', '', title)
            title = re.sub('\n', ' ', title)

            regex = re.compile('(\*{3}[^\*]*\*{3})')
            match_obj = regex.search(title)
            if match_obj:
                title = match_obj[0]

            title = re.sub('\*{3} START OF (THIS|THE) PROJECT GUTENBERG EBOOK ', '', title)
            title = title.replace('***', '').strip().title()
            return title


def scrape_url(url):
    full_path = get_page(url)
    soup = load_page(full_path)
    title = get_title(soup)
    filter_page(soup)
    text_list = soup.body.get_text(separator="\n", strip=True).split()
    book_dict = {'title': title,
                 'text_list': text_list}
    return book_dict


def pickle_all_urls():
    for url in URL_LIST:
        full_path = get_page(url)
        soup = load_page(full_path)
