import json


def load_posts():
    with open('posts.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def search_key(key):
    result = []
    for i in load_posts():
        if key.lower() in i['content'].lower():
            result.append(i)
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='UTF-8') as file:
        data = json.dump(posts, file, ensure_ascii=False)
    return
