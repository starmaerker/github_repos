import requests


def search_repos(lang):
    result = requests.get(f'https://api.github.com/search/repositories?q=language:{lang}&sort=stars&order=desc').json()

    counter = 0
    repo_list = {}
    while counter < 30:
        repo = result['items'][counter]
        repo_list[counter] = [repo['name'], repo['description'], repo['stargazers_count'], repo['owner']['avatar_url']]
        counter += 1
    return repo_list
