import json
import os
from dataclasses import dataclass

from dacite import from_dict


@dataclass(frozen=True)
class Logging:
    endpoint: str
    log_level: str


@dataclass(frozen=True)
class OtherSettings:
    foo: str


@dataclass(frozen=True)
class Config:
    logging: Logging
    other_settings: OtherSettings


def load():
    base_path = os.path.abspath(os.path.dirname(__file__))
    env = os.environ.get('STAGE', 'local')
    config_path = os.path.join(base_path, f"{env}.json")
    with open(config_path, 'r') as f:
        data = json.loads(f.read())
    return from_dict(data_class=Config, data=data)


config = load()
