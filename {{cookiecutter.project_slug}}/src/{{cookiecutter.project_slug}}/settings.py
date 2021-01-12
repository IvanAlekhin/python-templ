from dataclasses import asdict, dataclass
import threading

import uvloop
import asyncio

from tass_envmapping import BaseEnvMapping, field, EnvType

uvloop.install()
loop = asyncio.get_event_loop()

_conf = threading.local()
_conf.config = None


@dataclass(frozen=True)
class Settings(BaseEnvMapping):
    db_name: str = field(env_type=EnvType.string)
    db_max_con: int = field(env_type=EnvType.int)
    db_user: str = field(env_type=EnvType.string)
    db_password: str = field(env_type=EnvType.string)
    db_host: str = field(env_type=EnvType.string)
    db_port: int = field(env_type=EnvType.int)
    listen_port: int = field(env_type=EnvType.int)
    listen_host: str = field(env_type=EnvType.string)
    log_level: str = field(env_type=EnvType.string)


def build_config():
    if _conf.config:
        return _conf.config
    settings = Settings.create()
    _conf.config = settings
    return _conf.config


def represent_conf():
    skip_suffixes = ['password', 'secret']
    return {
        key: value for key, value in asdict(_conf.config).items()
        if all(key.find(skip) < 0 for skip in skip_suffixes)
    }
