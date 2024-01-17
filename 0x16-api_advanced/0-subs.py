#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


URL_BASE = 'https://www.reddit.com'
'''Base API URL.
'''


def number_of_subscribers(subreddit):
    '''Gets the number of subscribers in a subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    result = requests.get(
        '{}/r/{}/about/.json'.format(URL_BASE, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if result.status_code == 200:
        return result.json()['data']['subscribers']
    return 0
