from asana_app import asana_routers
from notion_app import notion_routers
from tweet_app import tweet_routers
from reddit_app import reddit_routers
from jina_scrapper_app import jina_routers
from fastapi import FastAPI
app = FastAPI()

app.include_router(asana_routers.router)
app.include_router(notion_routers.router)
app.include_router(tweet_routers.router)
app.include_router(reddit_routers.router)
app.include_router(jina_routers.router)
