FROM docker-registry.corp.tass.ru/core/python-docker-base:3.8-poetry-latest as build
WORKDIR {{cookiecutter.project_infra_name}}
COPY pyproject.toml pyproject.toml
RUN poetry config virtualenvs.in-project true && poetry install --no-dev
COPY README.MD README.MD
COPY src src
# Yes, again
RUN poetry install --no-dev

FROM python:3.8-slim
WORKDIR {{cookiecutter.project_infra_name}}
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo "Europe/Moscow" > /etc/timezone
COPY --from=build /{{cookiecutter.project_infra_name}} ./
ENV PATH=/{{cookiecutter.project_infra_name}}/.venv/bin:$PATH
EXPOSE 8788
ENTRYPOINT ["{{cookiecutter.project_infra_name}}-ctl"]
CMD ["server", "run"]
