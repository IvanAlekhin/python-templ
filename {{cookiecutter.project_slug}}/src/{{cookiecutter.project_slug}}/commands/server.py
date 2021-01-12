import os

import click

from {{cookiecutter.project_slug}}.commands import cli
from {{cookiecutter.project_slug}}.settings import build_config


if int(os.environ.get("NEW_RELIC_ENABLE", 0)) > 0:
    import newrelic.agent
    newrelic.agent.initialize()


@cli.group()
def server():
    pass


@server.command('run')
@click.option('--log_level', default=None, show_default=True, help='Log level')
def server_run(log_level: str = None):
    build_config()
    from {{cookiecutter.project_slug}}.log_manager import log_manager
    log_manager.setBaseLevel(log_level.upper() if isinstance(log_level, str) else log_level)
    from {{cookiecutter.project_slug}}.app import run
    run()
