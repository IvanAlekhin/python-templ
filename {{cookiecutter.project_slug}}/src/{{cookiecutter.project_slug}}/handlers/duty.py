from aiocache import SimpleMemoryCache
from aiocache.serializers import JsonSerializer
from aiohttp import web

from {{cookiecutter.project_slug}}.settings import represent_conf
from {{cookiecutter.project_slug}}.log_manager import log_manager

LOGGER = log_manager.getLogger(module_name=__name__)


cache = SimpleMemoryCache(serializer=JsonSerializer())


class HealthHandler(web.View):
    async def get(self):
        return web.json_response(dict(data=represent_conf()))
