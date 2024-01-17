#!/usr/bin/python3
'''module containing functions for working with the Reddit API.'''
import requests


base_url = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''Retrieves list of hot posts from a given subreddit.
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
    sort = 'hot'
    limit = 30
    result = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            base_url,
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if result.status_code == 200:
        data = result.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
