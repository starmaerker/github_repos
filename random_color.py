import random

color_list = ["btn-primary", "btn-secondary", "btn-success", "btn-danger", "btn-warning", "btn-info", "btn-light", "btn-dark"]


def create_list():
    result = []
    for _ in range(0, 12):
        result.append(color_list[random.randint(0, 7)])

    return result
