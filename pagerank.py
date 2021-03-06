'''
Author: Gutierrez Adrian
Updated: 21 March, 2020

Purpose: A simple python script 
that page ranks urls.
'''

from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
from collections import deque
import requests
import argparse
import signal
import re
import sys
import os

# set default score
score = 0.0

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

total_urls_visited = 0

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                # print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        # print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

def crawl(url, max_urls):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)
    if len(external_urls) is 0:
        score = 0.0
    else:
        rank = len(internal_urls) / len(external_urls)
        score = rank / max_urls
        tScore = lambda a : a * 0.85 + 0.15
        return tScore(score)

def main(argv):
    domain = argv
    for i in range(1):
        signal.alarm(10)
        # start page rank process
        score = crawl(domain, max_urls=1)
        print("Score:", round(score, 2))

if __name__ == "__main__":
    main(sys.argv[1])
