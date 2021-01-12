from {{cookiecutter.project_slug}}.handlers import duty, v1


routes = [
    ('*', '/_health', duty.HealthHandler, 'health'),
    ('*', '/api/v1/dummy', v1.DummyHandler, 'dummy'),
]
