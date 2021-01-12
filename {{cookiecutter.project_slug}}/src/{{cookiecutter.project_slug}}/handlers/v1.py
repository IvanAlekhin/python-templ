from aiocache import SimpleMemoryCache
from aiocache.serializers import JsonSerializer
from aiohttp import web
from aiohttp_apispec import docs, response_schema, use_kwargs
from marshmallow import ValidationError

from {{cookiecutter.project_slug}}.entities.requests import RequestPostDummy
from {{cookiecutter.project_slug}}.entities.responses import ResponseGetDummyData, ResponseGetDummy, \
    ResponseInternalError
from {{cookiecutter.project_slug}}.services.dummy import get_dummy, post_dummy
from {{cookiecutter.project_slug}}.log_manager import log_manager

LOGGER = log_manager.getLogger(module_name=__name__)

cache = SimpleMemoryCache(serializer=JsonSerializer())


class DummyHandler(web.View):
    @docs(tags=['dummy'],
          summary='Get dummy',
          description='''Dummy resource''')
    @response_schema(ResponseGetDummyData.Schema(), 200, description="Single dummy", required=True)
    @response_schema(ResponseInternalError.Schema(), 400, description="Error description", required=True)
    async def get(self):
        dummy = await get_dummy()
        try:
            payload = dummy.make_dump()
        except ValidationError as err:
            return web.json_response({"error": err.messages}, status=400)
        return web.json_response({"data": payload})


    @docs(tags=['dummy'],
          summary='Post new dummy',
          description='''Dummy resource''')
    @use_kwargs(RequestPostDummy.Schema())
    @response_schema(ResponseGetDummyData.Schema(), 200, description="Single dummy", required=True)
    @response_schema(ResponseInternalError.Schema(), 400, description="Error description", required=True)
    async def post(self):
        request_entity: RequestPostDummy  # for typing
        request_entity = self.request['validated_data']

        dummy = await post_dummy(request_entity.name, request_entity.nickname)  # if not nick_name in req, return none
        try:
            payload = dummy.make_dump()
        except ValidationError as err:
            return web.json_response({"error": err.messages}, status=400)
        return web.json_response({"data": payload})
