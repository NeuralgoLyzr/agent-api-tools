from pydantic import BaseModel

class PostData(BaseModel):
    subreddit_name: str
    title: str
    body: str
