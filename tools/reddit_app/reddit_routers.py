from fastapi import APIRouter,  HTTPException
from .models import PostData
from pydantic import BaseModel
import praw
from .config import CLIENT_ID, CLIENT_SECRET, USERNAME, USER_AGENT, PASSWORD

router = APIRouter()
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT,
                     username=USERNAME,
                     password=PASSWORD)


@router.post("/create_reddit_post/")
def create_post(post_data: PostData):
    try:
        subreddit = reddit.subreddit(post_data.subreddit_name)
        post = subreddit.submit(post_data.title, selftext=post_data.body)
        return {"message": "Post created successfully", "url": post.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
