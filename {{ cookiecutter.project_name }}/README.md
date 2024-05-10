# {{ cookiecutter.project_name }} prefect task


## Post-generation steps

- Ask Reinout to adjust the github permissions for the project.



## Local development

Using a "virtualenv" is the standard way of working on python projects in a neat and ordered and time-saving way:

    $ python3 -m venv .venv            # Only needed once
    $ .venv\Scripts\activate           # Activate on windows
    $ source .venv/bin/activate        # Activate on linux
    $ pip install -r requirements.txt  # Whenever requirements.txt changes

You can now run `python src/flows.py` and start experimenting. Tasks and flows should inititally go in `flows.py` and `tasks.py` (though you may split it over multiple files if handy). `src/server.py` is where you configure how you want to run those flows (as "deployments") on the task runner server in production.

Maintainability and some basic neatness is build-in. Make your life easy and pip-install `pre-commit` globally. Pre-commit does formatting checks, sorts your imports and so on. Github runs it automatically, so it is handy to do this locally first:

    $ pre-commit install

This will run pre-commit before every commit, preventing extra work :-)

If you use vscode and did the `.venv` thingy above, the python plugin will detect your code and prefect. So you'll have proper code completion! And type hints become more useful. Tip: also install [the vscode editorconfig plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) because that will automatically handle unneeded spaces at the end of lines and other minutia.

There are even tests files (see https://docs.pytest.org/ for instructions), you can use them to test calculations. Ask Reinout or Florian for tips. Don't test whether an ftp download can work, but *do* test when you do some real programming work.

Once the virtualenv is activated, you can run the tests simply with:

    $ pytest


## Running it on the server... happens automatically

It happens automatically after some one-time configuring:

- Github builds a new docker image for `main`.
- https://github.com/nens/prefect-setup has a `docker-compose.task.yml` that reloads new versions of the docker image and passes the `PREFECT_API_URL` environment variable.
- That docker runs your `server.py` with your configured deployments.
