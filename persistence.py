import json
from pathlib import Path
from typing import Dict, Any

DB_FILE = Path(__file__).parent / 'db.json'

def save(data: Dict[str, Any]):
    DB_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def load() -> Dict[str, Any]:
    if not DB_FILE.exists():
        return {}
    return json.loads(DB_FILE.read_text())