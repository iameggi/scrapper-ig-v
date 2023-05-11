import instaloader
from fastapi import FastAPI

app = FastAPI()

def scrape_instagram_content(username):
    
    loader = instaloader.Instaloader()

   
    profile = instaloader.Profile.from_username(loader.context, username)

   
    posts = list(profile.get_posts())[:6]

    content = []
    for post in posts:
      
        post_data = {
            'url': post.url,
            'caption': post.caption,
            'likes': post.likes,
            'comments': post.comments
        }
        content.append(post_data)

    return content

@app.get('/iameggi/api/v1/ig')
def scrape_handler(username: str):
    if not username:
        return {'error': 'Please provide a username'}
    scraped_content = scrape_instagram_content(username)

    return scraped_content
