import yaml
from pathlib import Path
from typing import Dict, Any

dtype_map = {
            "object": "text",
            "int64": "integer",
            "float64": "real"
        }

def get_config(path: str="config/config.yaml") -> Dict[str, Any]:
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
        
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file not found at {path}: {e}")
    
def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def sqlite3_dtype_map(dtype: str) -> str:
    try:
        return dtype_map[dtype]
    
    except Exception as e:
        raise Exception(f"Error mapping dtype: {e}")