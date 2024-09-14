from pydantic import BaseModel

class NotionPageRequest(BaseModel):
    notion_api_key: str
    notion_parent_page_id: str
    title: str
    content: str
