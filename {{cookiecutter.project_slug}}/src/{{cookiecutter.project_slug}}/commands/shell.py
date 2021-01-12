import importlib
import inspect
import os

import click
from ptpython.repl import embed

from {{cookiecutter.project_slug}}.commands import cli
from {{cookiecutter.project_slug}}.models.base import BaseModel


@cli.command('shell')
@click.option('--sqldebug', default=False, is_flag=True, help='Show all queries made by ORM')
def shell(sqldebug):
    models = importlib.import_module('{{cookiecutter.project_slug}}.models', package='{{cookiecutter.project_slug}}')
    locals_d = dict(models=models)
    for name, obj in inspect.getmembers(models):
        if inspect.isclass(obj) and issubclass(obj, BaseModel):
            locals_d[name] = obj
    if sqldebug:
        models.sql_debug(True)

    for name, obj in inspect.getmembers(models):
        locals_d[name] = obj

    embed(
        globals=locals_d,
        vi_mode=True,
        history_filename=os.path.join(os.path.expanduser('~'), '.{{cookiecutter.project_slug}}_cli_history'),
        title='{{cookiecutter.project_slug}} server shell',
    )
