posts = [
    {
        "id": 1,
        "title": "Sustainable Farming at Qaswa Agro",
        "content": "At Qaswa Agro, we believe in sustainable farming practices that nurture the environment.",
        "author": "Admin",
        "date": "2024-12-19"
    },
    {
        "id": 2,
        "title": "Innovative Agro Solutions",
        "content": "Discover our latest innovations in agriculture, tailored to meet global challenges.",
        "author": "Admin",
        "date": "2024-12-10"
    }
]

def get_posts():
    return posts

def get_post_by_id(post_id):
    return next((post for post in posts if post["id"] == post_id), None)

def add_post(title, content, author):
    new_post = {
        "id": len(posts) + 1,
        "title": title,
        "content": content,
        "author": author,
        "date": datetime.datetime.now().strftime("%Y-%m-%d")
    }
    posts.append(new_post)