from flask import Flask, render_template, url_for
from search import ergebnis

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def search_repos():
    results = ergebnis

    return render_template('index.html', results=results)


@app.route('/search/<lang>')
def search(lang):
    return render_template('search.html', lang=lang)


if __name__ == '__main__':
    app.run()
