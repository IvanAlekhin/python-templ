import re
import sys

PROJECT_SLUG_REGEX = r'^[_a-z0-9]{3,20}$'
PROJECT_INFRA_NAME_REGEX = r'^[-a-z0-9]{3,20}$'

project_slug = '{{ cookiecutter.project_slug }}'
project_infra_name = '{{ cookiecutter.project_infra_name }}'

if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print("""ERROR: The project slug "{}" is not a valid Python module name.
        It must contain between 3 and 20 characters.
        Please do not use capital letters, a "-" and use "_" instead.
        Example: "hello_world" """.format(project_slug))
    # Exit to cancel project
    sys.exit(1)

if not re.match(PROJECT_INFRA_NAME_REGEX, project_infra_name):
    print("""ERROR: The project infrastructure name "{}" is not a valid Python module name.
        It must contain between 3 and 20 characters.
        Please do not use capital letters, a "_" and use "-" instead.
        Example: "hello-world" """.format(project_infra_name))
    # Exit to cancel project
    sys.exit(1)
