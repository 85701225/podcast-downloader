#!/usr/bin/env python3
import configparser
import requests
import feedparser
import uuid

def get_config():
    c = configparser.ConfigParser()
    c.read('config.ini')
    rss_url = c.get('Default', 'rss')
    check_rss = c.get('Default', 'check_rss')
    return (rss_url, check_rss)

def download_rss(rss_url=None):
    if rss_url is not None:
        with open('rss.xml', 'w') as f:
            f.write(requests.get(rss_url).text)
    return None

def download_episodes():
    with open('rss.xml') as f:
        data = f.read()
        feed = feedparser.parse(data)
        for entry in feed.entries:
            print(f'Downloading {entry.title}')
            fn = 'episodes/' + entry.title.replace(' ', '_')
            with open(fn, 'wb') as out:
                out.write(requests.get(entry.links[1].href).content)

if __name__ == "__main__":
    rss_url = get_config()[0]
    check_rss = get_config()[1]
    if check_rss is True:
        # No elif, only download xml fresh if True
        download_rss(rss_url=rss_url)
    download_episodes()

"""
dict_keys(['title', 'title_detail', 'summary', 'summary_detail', 'links', 'link', 'id', 'guidislink', 'authors', 'author', 'author_detail', 'published', 'published_parsed', 'content', 'itunes_explicit', 'itunes_duration', 'image', 'itunes_episodetype'])
"""
