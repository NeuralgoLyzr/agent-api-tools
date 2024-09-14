from .models import TweetRequest
import tweepy
from fastapi import APIRouter, HTTPException
from .config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN

router = APIRouter()
client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)


@router.post("/create-tweet")
def create_tweet(request: TweetRequest):
    try:
        # Create the tweet
        response = client.create_tweet(text=request.text)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
