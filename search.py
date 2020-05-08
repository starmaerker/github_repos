import requests
from config import Config


def search_complete():
    languages = ['python', 'java', 'javascript', 'csharp', 'swift', 'haskell', 'php', 'ruby', 'dart', 'kotlin', 'c',
                 'go',
                 'r', 'scala', 'c%2B%2B', 'rust', 'powershell', 'html', 'css', 'typescript']
    complete_dic = {}
    for _ in languages:
        star_counter = 0
        result = requests.get(
            f'https://api.github.com/search/repositories?q=stars:>=1000 language:{_}&sort=stars&order=desc&per_page=20',
            auth=(Config.USERNAME, Config.TOKEN)).json()
        print(result)
        for item in range(0, len(result['items'])):
            repo = result['items'][item]
            star_counter += repo['stargazers_count']

        complete_dic[_] = star_counter

    return complete_dic


def search_repos(lang):
    star_counter = 0
    result = requests.get(
        f'https://api.github.com/search/repositories?q=stars:>=1000 language:{lang}&sort=stars&order=desc&per_page=42').json()
    repo_list = {}
    for counter in range(0, len(result['items'])):
        repo = result['items'][counter]
        repo_list[counter] = [repo['name'], repo['description'], repo['stargazers_count'], repo['owner']['avatar_url'],
                              repo['html_url']]
        star_counter += repo['stargazers_count']

    return repo_list, star_counter
