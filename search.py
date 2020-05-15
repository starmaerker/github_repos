import requests
from app import db
from model import Lang
from datetime import datetime


def search_repos(lang, username, token):
    star_counter = 0
    result = requests.get(
        f'https://api.github.com/search/repositories?q=stars:>=1000 language:{lang}&sort=stars&order=desc&per_page=42',
        auth=(username, token)).json()
    repo_list = {}
    for counter in range(0, len(result['items'])):
        repo = result['items'][counter]
        repo_list[counter] = [repo['name'], repo['description'], repo['stargazers_count'], repo['owner']['avatar_url'],
                              repo['html_url']]
        star_counter += repo['stargazers_count']

    entry = Lang(name=lang, stargazers=star_counter)
    from_db = Lang.query.filter_by(name=lang).first()

    if from_db is None:
        db.session.add(entry)
        db.session.commit()
    else:
        from_db.stargazers = star_counter
        from_db.timestamp = datetime.utcnow()
        db.session.commit()

    return repo_list, star_counter

