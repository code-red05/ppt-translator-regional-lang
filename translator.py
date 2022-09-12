import requests
def eng_to_hin(s):
    headers = {
    'authority': 'translate.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'dnt': '1',
    'accept': '*/*',
    'origin': 'http://www.easyhindityping.com',
    'x-client-data': 'CLC1yQEIk7bJAQijtskBCMG2yQEIqZ3KAQiTrMoBCIa1ygEI/7zKAQjnyMoBCLTLygE=',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'http://www.easyhindityping.com/english-to-hindi-translation',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    params = (
        ('client', 'gtx'),
        ('sl', 'en'),
        ('tl', 'hi'),
        ('dt', 't'),
        ('q', f'{s}'),
    )

    response = requests.get('https://translate.googleapis.com/translate_a/single', headers=headers, params=params)
    a=response.text
    return a.split('"')[1]
def eng_to_tam(s):
    headers = {
    'authority': 'translate.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'dnt': '1',
    'accept': '*/*',
    'origin': 'http://www.easyhindityping.com',
    'x-client-data': 'CLC1yQEIk7bJAQijtskBCMG2yQEIqZ3KAQiTrMoBCIa1ygEI/7zKAQjnyMoBCLTLygE=',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'http://www.easyhindityping.com/english-to-tamil-translation',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    params = (
        ('client', 'gtx'),
        ('sl', 'en'),
        ('tl', 'ta'),
        ('dt', 't'),
        ('q', f'{s}'),
    )

    response = requests.get('https://translate.googleapis.com/translate_a/single', headers=headers, params=params)
    a=response.text
    return a.split('"')[1]
def eng_to_mar(s):
    headers = {
    'authority': 'translate.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'dnt': '1',
    'accept': '*/*',
    'origin': 'http://www.easyhindityping.com',
    'x-client-data': 'CLC1yQEIk7bJAQijtskBCMG2yQEIqZ3KAQiTrMoBCIa1ygEI/7zKAQjnyMoBCLTLygE=',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'http://www.easyhindityping.com/english-to-marathi-translation',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    params = (
        ('client', 'gtx'),
        ('sl', 'en'),
        ('tl', 'mr'),
        ('dt', 't'),
        ('q', f'{s}'),
    )

    response = requests.get('https://translate.googleapis.com/translate_a/single', headers=headers, params=params)
    a=response.text
    return a.split('"')[1]