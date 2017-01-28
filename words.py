"""Retrieve and print words from a URL.

Usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    :param url:The URL of a UTF-8 text document.

    :return: A list of strings containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(story_words):
    """Print items one per line

    :param story_words: An iterable series of printable items.
    """
    for word in story_words:
        print(word)


def main(url_path):
    """Print each word from a text document from a URL.

    :param url_path: The URL of a UTF-8 text focument.
    """
    words = fetch_words(url_path)
    print_items(words)


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)


def min_max(items):
    return min(items), max(items)
