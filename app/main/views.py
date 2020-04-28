from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article_by_source

@main.route('/')
def index():
    sources = get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/articles/<id>')
def source_article(id):
    source_articles = get_article_by_source(id)
    id = id
    return render_template('articles.html', source_articles=source_articles, id=id)