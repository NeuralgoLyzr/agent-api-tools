from tools.asana_app import asana_routers
from tools.notion_app import notion_routers
from tools.tweet_app import tweet_routers
# from tools.reddit_app import reddit_routers
from tools.jina_scrapper_app import jina_routers
from fastapi import FastAPI

app = FastAPI()

app.include_router(asana_routers.router, tags=["Asana"], prefix="/asana")
app.include_router(notion_routers.router, tags=["Notion"], prefix="/notion")
app.include_router(tweet_routers.router, tags=["Twitter"], prefix="/tweets")
# app.include_router(reddit_routers.router, tags=["Reddit"], prefix="/reddit")
app.include_router(jina_routers.router, tags=["Jina"], prefix="/jina")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8320, reload=True)
