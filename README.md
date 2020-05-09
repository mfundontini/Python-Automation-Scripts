# Python-Automation-Scripts

A folder of automation scripts written in Python. These are just for testing so if I never actually add any code forgive me future me.

# PipEnv

These projects use pipenv instead of vanilla pip, here is a quick primer:

`virtualenv -p <python version> ve` -> `pipenv install --python <python version>` 

`pip install <package>` -> `pipenv install <package>`

`pip install -r <package-file>` -> `pipenv install -r <package-file>`

`pip freeze` -> `pipenv lock -r`

`pip uninstall <package>` -> `pipenv uninstall <package>`

In order to activate the venv `pipenv shell` or simply run your scripts in the format `pipenv run <script>`. Thus running
a django server will be `pipenv run ./manage.py runserver`, of course depending on the directory structure. Pip env also checks
for a `.env` file and injects environment variables in the virtual environment.

To remove an environment you can either run `pipenv --rm` && `pipenv install` if there is a pipfile with a specified python or 
run `pipenv install --python <python version>`. `pipenv lock` will lock your current packages and dependencies and thus allow you to run
your application in production after `pipenv install --ignore-pipfile`.

Pipenv allows you to check your dependency graph via `pipenv graph`, check for vulnerabilities with `pipenv check` and the location
 of your venv with `ppenv --venv`. If you run the virtualenv with `pipenv shell`, then you exit the shell with `exit` as it is actually a sub shell/terminal.
 Note that pipenv still uses most of the pip and virtualenv existing API and by knowing where the venv is, one can still use the old API.
