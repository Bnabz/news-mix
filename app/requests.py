import requests

from config import Config

api_key = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_sources(self):
    sources = []
    sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, self.API_KEY)
    response = requests.get(sources_url)
    if response.status_code == 200:
        for data in response.json()['sources']:
            sources.append(data)
        print(sources)
        return sources