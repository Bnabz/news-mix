from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    sources = get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/article/<id>')
def source_article(id):
    source_articles = news_request_handler.get_article_by_source(id)
    source = id
    return render_template('articles_display.html', source_articles=source_articles, source=source)