from aiocache import SimpleMemoryCache

from {{cookiecutter.project_slug}}.settings import build_config


build_config()


def setup_cache():
    cache = SimpleMemoryCache(ttl=10)
    return cache


cache = setup_cache()
