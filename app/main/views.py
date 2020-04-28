from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    sources = get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/articles')
def view_articles():
    articles = get_articles("tech")
    return render_template('articles.html', articles=articles)