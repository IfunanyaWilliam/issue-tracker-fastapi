from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"
USERS_FILE = DATA_DIR / "users.json"

def load_data(file_path: Path = DATA_FILE, limit: int | None = None, offset: int = 0):
    if file_path.exists():
        with open(file_path, "r") as f:
            content = f.read()
            if content.strip():  # Check if the file is not empty
                data = json.loads(content)
                if limit is None:
                    return data[offset:]
                return data[offset:offset + limit]
    return []

def save_data(data, file_path: Path = DATA_FILE):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
