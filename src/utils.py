import yaml
from pathlib import Path
from typing import Dict, Any

def get_config(path: str="config/config.yaml") -> Dict[str, Any]:
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
        
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file not found at {path}: {e}")
    
def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)