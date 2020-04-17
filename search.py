import requests

result = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc').json()


def search_repos():
    counter = 0
    repo_list = {}
    while counter < 20:

        repo = result['items'][counter]

        repo_list[counter] = [repo['name'], repo['description'], repo['stargazers_count']]

        # print(f"{counter+1}. {repo['name']} Beschreibung: {repo['description']} Stars: {repo['stargazers_count']}")
        counter += 1

    return repo_list


ergebnis = search_repos()




