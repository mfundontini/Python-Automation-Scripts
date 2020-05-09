# Python-Automation-Scripts

A folder of automation scripts written in Python.

# PipEnv

These projects use pipenv instead of vanilla pip, here is a quick primer:

`virtualenv -p <python version> ve` -> `pipenv install --python <python version>` 

`pip install <package>` -> `pipenv install <package>`

`pip freeze` -> `pipenv lock -r`

`pip uninstall <package>` -> `pipenv uninstall <package>`

In order to activate the venv `pipenv shell` or simply run your scripts in the format `pipenv run <script>`. Thus running
a django server will be `pipenv run python manage.py runserver`
