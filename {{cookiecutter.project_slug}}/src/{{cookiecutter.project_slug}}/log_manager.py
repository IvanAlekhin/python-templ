from tass_log_manager.tass_log_manager import LogManager
from {{cookiecutter.project_slug}}.settings import build_config, _conf as config

build_config()

log_manager = LogManager('{{cookiecutter.project_slug}}', config.config.log_level)
