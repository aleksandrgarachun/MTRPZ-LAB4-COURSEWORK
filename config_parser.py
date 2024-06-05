import yaml
from typing import Dict, Any

class ConfigParser:
    def __init__(self, config_file: str):
        self.config_file = config_file

    def parse(self) -> Dict[str, Any]:
        """
        Завантажує та парсить конфігураційний файл YAML.
        """
        with open(self.config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config