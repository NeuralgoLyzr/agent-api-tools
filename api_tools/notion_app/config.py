import os
from dotenv import load_dotenv

load_dotenv()

ASANA_KEY = os.getenv("ASANA_TOKEN")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
