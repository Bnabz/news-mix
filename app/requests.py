import urllib.request,json
from .models import Article
import requests



api_key = None

sources_url = None

def configure_request(app):
	global api_key,sources_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	# sources_url = app.config['NEWS_SOURCES_BASE_URL']
	# articles_url = app.config['ARTICLES_BASE_URL']

# def get_sources():
#     get_news_sources_url = sources_url.format(api_key)


#     with urllib.request.urlopen(get_news_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         sources = None

#         if get_sources_response['sources']:
#             sources = get_sources_response['sources']
            
#     return sources

def get_sources(self):
    sources = []
    sources_url = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources, api_key)
    response = requests.get(sources_url)
    if response.status_code == 200:
        for data in response.json()['sources']:
            sources.append(data)
        print(sources)
    return sources


    

