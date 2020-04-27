import requests


def search_repos(lang):
    result = requests.get(
        f'https://api.github.com/search/repositories?q=stars:>=1000 language:{lang}&sort=stars&order=desc&per_page=42').json()
    incomplete = result['incomplete_results']
    repo_list = {}
    for counter in range(0, len(result['items'])):
        repo = result['items'][counter]
        repo_list[counter] = [repo['name'], repo['description'], repo['stargazers_count'], repo['owner']['avatar_url'],
                              repo['html_url']]

    return repo_list, incomplete
