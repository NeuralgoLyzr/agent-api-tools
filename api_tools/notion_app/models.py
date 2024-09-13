from pydantic import BaseModel

class NotionPageRequest(BaseModel):
    notion_parent_page_id: str
    title: str
    content: str
