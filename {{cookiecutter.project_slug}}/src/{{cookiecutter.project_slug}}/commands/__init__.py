from {{cookiecutter.project_slug}}.commands.base import cli
from {{cookiecutter.project_slug}}.commands.server import server  # noqa
from {{cookiecutter.project_slug}}.commands.shell import shell  # noqa


if __name__ == '__main__':
    cli(obj={})
