import urllib.request,json
from .models import Article
import requests
from newsapi import NewsApiClient



api_key = None

sources_url = None

def configure_request(app):
	global api_key,sources_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	# sources_url = app.config['NEWS_SOURCES_BASE_URL']
	# articles_url = app.config['ARTICLES_BASE_URL']

newsapi = NewsApiClient(api_key='4d2a9b72117b4ae0a28523b8a5a092e2')


def get_sources():
    sources = []
    sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, api_key)
    response = requests.get(sources_url)
    if response.status_code == 200:
        for data in response.json()['sources']:
            sources.append(data)
    return sources



def get_articles(article):
        articles = []
        articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, api_key)
        response = requests.get(articles_url)
        if response.status_code == 200:
            for data in response.json()['articles']:
                articles.append(data)
            return articles



# def get_sources():
#     sources = newsapi.get_sources()
#     print("hello")
#     return sources


    

