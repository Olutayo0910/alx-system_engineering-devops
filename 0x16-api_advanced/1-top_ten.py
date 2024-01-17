#!/usr/bin/python3
'''module containing functions for working with the Reddit API.'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.'''


def top_ten(subreddit):
    '''Retrieves title of top ten posts from a given subreddit.'''
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
    sort = 'top'
    limit = 10
    result = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if result.status_code == 200:
        for post in result.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
