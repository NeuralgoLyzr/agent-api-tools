from fastapi import APIRouter, HTTPException
from .models import TaskCreateRequest, ProjectCreateRequest, CustomFieldCreateRequest
import asana

router = APIRouter()

@router.post("/create-task")
async def create_task(request: TaskCreateRequest):
    try:
        client = asana.Client.access_token(request.pat_token)
        task = client.tasks.create_task({
            'workspace': request.workspace_id,
            'projects': [request.project_id],
            'name': request.name,
            'notes': request.notes,
            'followers': request.followers,
            'assignee': request.assignee,
            'due_on': request.due_on,
        })
        return {"task_id": task['gid'], "task_name": task['name']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create-project")
async def create_project(request: ProjectCreateRequest):
    try:
        client = asana.Client.access_token(request.pat_token)
        project = client.projects.create_project({
            'workspace': request.workspace_id,
            'name': request.name,
            'notes': request.notes,
            'privacy_setting': request.privacy_setting,
            'due_on': request.due_on,
        })
        return {"project_id": project['gid'], "project_name": project['name']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/task/{task_id}")
async def get_task(task_id: str, pat_token: str):
    try:
        client = asana.Client.access_token(pat_token)
        task = client.tasks.get_task(task_id)
        return {
            "task_id": task['gid'],
            "name": task['name'],
            "notes": task['notes'],
            "assignee": task.get('assignee', None),
            "due_on": task.get('due_on', None),
            "completed": task['completed']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create-custom-field")
async def create_custom_field(request: CustomFieldCreateRequest):
    try:
        client = asana.Client.access_token(request.pat_token)
        data = {
            'name': request.name,
            'type': request.field_type,
            'workspace': request.workspace_id
        }

        if request.field_type == 'enum' and request.options:
            data['enum_options'] = [{'name': option} for option in request.options]

        custom_field = client.custom_fields.create_custom_field(data)
        client.projects.add_custom_field_setting(request.project_id, {
            'custom_field': custom_field['gid'],
            'precision': '0'
        })

        return {"custom_field_id": custom_field['gid'], "name": custom_field['name'], "options": custom_field.get('enum_options', [])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{workspace_id}")
async def get_users(workspace_id: str, pat_token: str):
    try:
        client = asana.Client.access_token(pat_token)
        users = client.users.get_users_for_workspace(workspace_id)
        return [{"user_id": user['gid'], "name": user['name']} for user in users]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/workspaces")
async def get_workspaces(pat_token: str):
    try:
        client = asana.Client.access_token(pat_token)
        workspaces = client.workspaces.find_all()
        return [{"workspace_id": workspace['gid'], "name": workspace['name']} for workspace in workspaces]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/projects/{workspace_id}")
async def get_projects(workspace_id: str, pat_token: str):
    try:
        client = asana.Client.access_token(pat_token)
        projects = client.projects.find_by_workspace(workspace_id)
        return [{"project_id": project['gid'], "name": project['name']} for project in projects]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tasks/{project_id}")
async def get_tasks(project_id: str, pat_token: str):
    try:
        client = asana.Client.access_token(pat_token)
        tasks = client.tasks.get_tasks_for_project(project_id)
        return [{"task_id": task['gid'], "task_name": task['name']} for task in tasks]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
