from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    sources = get_sources
    print(sources)
    if sources:
        return render_template('index.html', sources=sources)