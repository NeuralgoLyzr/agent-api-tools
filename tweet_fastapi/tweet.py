import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tweepy
from dotenv import load_dotenv

load_dotenv()


# Define your API keys and tokens here (make sure to keep them secure)

# Initialize Tweepy client
client = tweepy.Client(consumer_key=os.getenv("CONSUMER_KEY"),
                       consumer_secret=os.getenv("CONSUMER_SECRET"),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

# Initialize FastAPI
app = FastAPI()

# Define a request body model for the tweet
class TweetRequest(BaseModel):
    text: str

@app.post("/tweet")
def create_tweet(request: TweetRequest):
    try:
        # Create the tweet
        response = client.create_tweet(text=request.text)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
