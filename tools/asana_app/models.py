from pydantic import BaseModel

class TaskCreateRequest(BaseModel):
    pat_token: str
    workspace_id: str
    project_id: str
    name: str
    notes: str
    followers: list[str]
    assignee: str
    due_on: str

class ProjectCreateRequest(BaseModel):
    pat_token: str
    workspace_id: str
    name: str
    notes: str
    privacy_setting: str
    due_on: str

class TaskUpdateRequest(BaseModel):
    pat_token:str
    task_id: str

class CustomFieldCreateRequest(BaseModel):
    pat_token: str
    workspace_id: str
    project_id: str
    name: str
    field_type: str  # e.g., "text", "number", "enum"
    options: list[str] = []
