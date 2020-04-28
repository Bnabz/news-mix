from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    sources = get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/technology')
def tech_articles():
    articles = get_articles("tech")
    return render_template('articles.html', articles=articles)

@main.route('/business')
def biz_articles():
    articles = get_articles("business")
    return render_template('articles.html', articles=articles)

@main.route('/business')
def viewb_articles():
    articles = get_articles("entertainment")
    return render_template('articles.html', articles=articles)