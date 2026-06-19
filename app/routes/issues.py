import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueStatus, IssuePriority
from app.storage import load_data, save_data



router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/", response_model=list[IssueOut])
async def get_issues():
    '''Retrieve all issues from the storage.'''
    issues = load_data()
    return issues

@router.get("/{issue_id}", response_model=IssueOut)
async def get_issue(issue_id: str):
    '''Retrieve a specific issue by its ID.'''
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue(payload: IssueCreate):
    '''Create a new issue and save it to the storage.'''
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "status": IssueStatus.open.value,
        "priority": payload.priority.value
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue


@router.put("/{issue_id}", response_model=IssueOut)
async def update_issue(issue_id: str, payload: IssueUpdate):
    '''Update an existing issue by its ID.'''
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()
            if payload.title is not None:
                updated_issue["title"] = payload.title
            if payload.description is not None:
                updated_issue["description"] = payload.description
            if payload.status is not None:
                updated_issue["status"] = payload.status.value
            if payload.priority is not None:
                updated_issue["priority"] = payload.priority.value
            issues[index] = updated_issue
            save_data(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_issue(issue_id: str):
    '''Delete an existing issue by its ID.'''
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            del issues[index]
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
