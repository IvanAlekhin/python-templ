from json.decoder import JSONDecodeError

import peewee
from aiohttp import web
from aiomysql import OperationalError
from tass_apispec import validation_middleware, setup_tass_apispec

from {{cookiecutter.project_slug}}.handlers import _preflight_handler
from {{cookiecutter.project_slug}}.routes import routes
from {{cookiecutter.project_slug}}.settings import _conf as config
from {{cookiecutter.project_slug}}.settings import loop
from {{cookiecutter.project_slug}}.log_manager import log_manager

LOGGER = log_manager.getLogger(module_name=__name__)


@web.middleware
async def internal_error_middleware(request, handler):
    try:
        return await handler(request)
    except (peewee.OperationalError, peewee.ProgrammingError, OperationalError, JSONDecodeError) as exc:
        resp = web.json_response({"error": "Error: {}. Desc: {}".format(type(exc), str(exc))}, status=400)
        return await _preflight_handler(request, resp)


def make_app(app):
    for r in routes:
        app.router.add_route(r[0], r[1], r[2], name=r[3])
    setup_tass_apispec(app=app, title="API documentation", version="v1",
                          request_data_name='validated_data', swagger_path='/api/doc',
                          static_path="/api/static/swagger")
    app.middlewares.extend([internal_error_middleware, validation_middleware])
    return app


def run():
    app = web.Application(loop=loop)
    make_app(app)
    web.run_app(app, host=config.config.listen_host, port=config.config.listen_port)
