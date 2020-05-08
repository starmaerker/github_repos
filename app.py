from flask import Flask, render_template, url_for
from search import search_repos
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<lang>')
def search(lang):
    results, star_counter = search_repos(lang)
    return render_template('search.html', lang=lang, results=results, star_counter=star_counter)


if __name__ == '__main__':
    app.run()
