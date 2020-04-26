from flask import Flask, render_template, url_for
from search import search_repos


app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<lang>')
def search(lang):
    results = search_repos(lang)
    return render_template('search.html', lang=lang, results=results)


if __name__ == '__main__':
    app.run()
