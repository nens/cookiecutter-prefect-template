# {{ cookiecutter.project_name }} prefect task


## Post-generation steps

- Ask Reinout to adjust the github permissions for the project.



## Local development

Using a "virtualenv" is the standard way of working on python projects in a neat and ordered and time-saving way:

    $ python3 -m venv .venv        # Only needed once
    $ Scripts/activate.bat         # Or however activation works on windows
    $ pip install -r requirements  # After activation

You can now run `python src/flows.py` and start experimenting. Tasks and flows should inititally go in there (though you may split it over multiple files if handy). `src/server.py` is where you configure how you want to run those flows (as "deployments") on the task runner server in production.

Maintainability and some basic neatness is build-in. Make your life easy and pip-install `pre-commit` globally (and [the vscode editorconfig plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) if you use vscode).

Pre-commit does formatting checks, sorts your imports and so on. Github runs it automatically, so it is handy to do this locally:

    $ pre-commit install

This will run pre-commit before every commit, preventing extra work :-)


## Running it on the server... happens automatically

It happens automatically after some one-time configuring:

- Github builds a new docker image for `main`.
- https://github.com/nens/prefect-setup has a `docker-compose.task.yml` that reloads new versions of the docker image and passes the `PREFECT_API_URL` environment variable.
- That docker runs your `server.py` with your configured deployments.
