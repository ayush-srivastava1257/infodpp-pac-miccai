import yaml
from pathlib import Path

def load_config(path):
    """
    Load YAML configuration file.
    Returns a Python dict.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    return config
