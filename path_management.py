from pathlib import Path
import os


def get_project_root():
    return Path(__file__).parent


def get_bookname_from_url(url):
    page = url.split('/')[-1]
    name = page.split('.')[0]
    return name


def get_bookfolder():
    root_folder = get_project_root()
    book_folder = os.path.join(root_folder, 'Files', 'Books')
    return book_folder


def get_bookpath(url):
    name = get_bookname_from_url(url)
    book_folder = get_bookfolder()
    bookpath = os.path.join(book_folder, f'{name}.pickle')
    return bookpath


def book_downloaded(url):
    bookpath = get_bookpath(url)
    return os.path.isfile(bookpath)


if __name__ == '__main__':
    print(get_project_root())
