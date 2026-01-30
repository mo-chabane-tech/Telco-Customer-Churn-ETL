import logging
import logging.config
from typing import Dict, Any
from src.utils import ensure_dir
from pathlib import Path

def setup_logger(config: Dict[str, Any]) -> None:
    try:
        log_path: Path = Path(config["paths"]["logs_file"])
        ensure_dir(log_path.parent)
        logging.config.dictConfig(config["logging"])
        logging.info("Logger configured successfully.")

    except Exception as e:
        print(f"Error configuring logger: {e}")
        raise