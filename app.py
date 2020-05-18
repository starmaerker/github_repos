from flask import Flask, render_template, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Lang': Lang}


@app.route('/index')
@app.route('/')
def index():
    # list_db = db.session.query(Lang).order_by(Lang.stargazers.desc()).all()

    result = db.engine.execute("SELECT name, real_name FROM lang ORDER BY stargazers DESC")
    search_names = [(row[0], row[1]) for row in result]

    return render_template('index.html', search_names=search_names)


@app.route('/search/<lang>')
def search(lang):
    results, star_counter = search_repos(lang, app.config['USERNAME'], app.config['TOKEN'])
    return render_template('search.html', lang=lang, results=results, star_counter=star_counter)


if __name__ == '__main__':
    app.run()

from search import search_repos
from model import Lang
