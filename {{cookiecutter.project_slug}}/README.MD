{{cookiecutter.project_slug}}
===========
{{cookiecutter.project_short_description}}

Quick Run
---------
```bash
cd {{cookiecutter.project_slug}}
poetry install && poetry shell
# if you are using direnv
cp .env.example .env
direnv allow
```

Docker usage:
```
docker build -t {{cookiecutter.project_slug}} .
docker run -p 8788:8788 --env-file .env {{cookiecutter.project_slug}}
```

For local development we strongly recommend using [direnv](https://direnv.net/)
Configure .env file or set OS environments:

* **listen_port** - Port, that app will listen
* **listen_host** - Host, that app will listen
* **db_name** - Database name
* **db_max_con** - Max database connection for poll
* **db_user** - Database user name
* **db_password** - Password for database user
* **db_host** - Host for DB instance
* **db_port** - Database port
* **log_level** - App's default log level

Run server with command:
```bash
{{cookiecutter.project_infra_name}}-ctl server run
```
