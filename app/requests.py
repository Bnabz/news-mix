import urllib.request,json
from .models import Article



api_key = None

def configure_request(app):
	global api_key,base_url,articles_url
	api_key = app.config('NEWS_API_KEY')
	sources_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']

def get_sources():
    get_news_sources_url = news_sources_url.format(api_key)
    get_sources_response = requests.get(get_news_sources_url).json()

    return get_sources_response["sources"]

