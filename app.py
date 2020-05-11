from flask import Flask, render_template, url_for
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<lang>')
def search(lang):
    results, star_counter = search_repos(lang, app.config['USERNAME'], app.config['TOKEN'])
    return render_template('search.html', lang=lang, results=results, star_counter=star_counter)


if __name__ == '__main__':
    app.run()


from search import search_repos
