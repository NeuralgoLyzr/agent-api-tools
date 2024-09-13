from fastapi import APIRouter, HTTPException
from .models import NotionPageRequest
import asana
from .config import ASANA_KEY, NOTION_API_KEY
import requests
import json

router = APIRouter()
client = asana.Client.access_token(ASANA_KEY)



def create_notion_page(notion_api_key, notion_parent_page_id, title, content):
    url = 'https://api.notion.com/v1/pages'

    headers = {
        'Authorization': f'Bearer {notion_api_key}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }

    data = {
        "parent": {"type": "page_id", "page_id": notion_parent_page_id},
        "properties": {
            "title": [
                {
                    "text": {
                        "content": title
                    }
                }
            ]
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "text": {
                                "content": content
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.post("/create-notion-page/")
async def create_page(request: NotionPageRequest):
    try:
        response = create_notion_page(
            notion_api_key=NOTION_API_KEY,
            notion_parent_page_id=request.notion_parent_page_id,
            title=request.title,
            content=request.content
        )
        return {"status": "success", "data": response}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)