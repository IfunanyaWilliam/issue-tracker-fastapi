```md
# Issue Tracker API

REST API for managing issues and tickets.

## Base URL

- `http://localhost:8000` (adjust if your app uses a different host/port)
- All endpoints are under: `/api/v1`

## Endpoints

### Get all issues
- **GET** `/api/v1/issues/`
- **Description:** Retrieve all issues from the storage.
- **Responses:**
  - `200` - Returns an array of `IssueOut`

---

### Create an issue
- **POST** `/api/v1/issues/`
- **Description:** Create a new issue and save it to the storage.
- **Request Body:** `IssueCreate` (JSON)
- **Responses:**
  - `201` - Returns the created `IssueOut`
  - `422` - Validation error

---

### Get an issue by ID
- **GET** `/api/v1/issues/{issue_id}`
- **Description:** Retrieve a specific issue by its ID.
- **Path Params:**
  - `issue_id` (string, required)
- **Responses:**
  - `200` - Returns `IssueOut`
  - `422` - Validation error

---

### Update an issue by ID
- **PUT** `/api/v1/issues/{issue_id}`
- **Description:** Update an existing issue by its ID.
- **Path Params:**
  - `issue_id` (string, required)
- **Request Body:** `IssueUpdate` (JSON, required)
- **Responses:**
  - `200` - Returns updated `IssueOut`
  - `422` - Validation error

---

### Delete an issue by ID
- **DELETE** `/api/v1/issues/{issue_id}`
- **Description:** Delete an existing issue by its ID.
- **Path Params:**
  - `issue_id` (string, required)
- **Responses:**
  - `204` - Deleted successfully
  - `422` - Validation error

## Models (Schemas)

### `IssuePriority`
- One of: `low`, `medium`, `high`

### `IssueStatus`
- One of: `open`, `in_progress`, `closed`

### `IssueCreate`
Fields:
- `title` (string)
  - minLength: 3
  - maxLength: 100
- `description` (string)
  - minLength: 5
  - maxLength: 1000
- `priority` (string, optional)
  - enum: `low | medium | high`
  - default: `medium`

### `IssueUpdate`
All fields are optional and may be `null`:
- `title`: string (3–100) or `null`
- `description`: string (5–1000) or `null`
- `status`: `open | in_progress | closed` or `null`
- `priority`: `low | medium | high` or `null`

### `IssueOut`
Fields (required):
- `id` (string)
- `title` (string)
- `description` (string)
- `status` (`open | in_progress | closed`)
- `priority` (`low | medium | high`)

### `HTTPValidationError`
Returned on request validation failures:
- `detail`: array of `ValidationError`

### `ValidationError`
Fields:
- `loc` (array of strings/integers)
- `msg` (string)
- `type` (string)
- `input` (optional)
- `ctx` (optional)

## Setup

### 1) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

### 2) Install dependencies
A `requirements.txt` file is included.

```bash
pip install -r requirements.txt
```

### 3) Run the API
How you run it depends on your project (e.g., `uvicorn`, `gunicorn`, etc.). Common patterns:
```bash
uvicorn main:app --reload
```

## Example Requests

### Create an issue
```bash
curl -X POST "http://localhost:8000/api/v1/issues/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Login button broken",
    "description": "The login button does nothing when clicked.",
    "priority": "high"
  }'
```

### List issues
```bash
curl -X GET "http://localhost:8000/api/v1/issues/"
```

### Get one issue
```bash
curl -X GET "http://localhost:8000/api/v1/issues/<issue_id>"
```

### Update an issue
```bash
curl -X PUT "http://localhost:8000/api/v1/issues/<issue_id>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "in_progress",
    "priority": "medium"
  }'
```

### Delete an issue
```bash
curl -X DELETE "http://localhost:8000/api/v1/issues/<issue_id>"
```

## Notes / Assumptions

- This README documents the API surface based on the provided OpenAPI spec.
- If your server uses a different host/port than `localhost:8000`, update the examples accordingly.
```