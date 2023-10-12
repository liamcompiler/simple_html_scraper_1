import requests
from bs4 import BeautifulSoup

def get_h1_tags(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to retrieve the page: {response.status_code}')

    soup = BeautifulSoup(response.content, 'html.parser')
    h1_tags = [tag.text for tag in soup.find_all('h1')]

    return h1_tags

# Usage:
url = 'https://example.com'
h1_data = get_h1_tags(url)
print(h1_data)
