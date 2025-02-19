# {{ cookiecutter.project_name }} prefect task

## Post-generation checklist

First a little bit of github administration:

- [ ] Just making sure: you created a github repo and did the init/add/push shown after generating the project?
- [ ] Go to the ["manage access" page](https://github.com/nens/{{ cookiecutter.project_name }}/settings/access) and click "add teams": add the "adviseurs" team with **write** access. Otherwise you're the only one who can work on it.
- [ ] On that same page, add the team "nelen-schuurmans-pull-only" with **read** access. Otherwise the server cannot download the docker image.

If you're working on other prefect tasks, you probably have these two installed already:

- [ ] Instead of virtualenv&pip, we now use `uv`. It handles the virtualenv, the pip install, pinning versions. It also works much faster. You need to install it, [here are the instructions](https://docs.astral.sh/uv/getting-started/installation/).
- [ ] To keep the code readable and maintainable, we use pre-commit. Install it with `pip install pre-commit` .

Lastly a bit of readme cleanup:

- [ ] In the next section, quickly add an initial sentence about the project.
- [ ] Remove this whole post-generation checklist from the readme. You won't need it anymore as you've diligently checked off every item :-)


## Project documentation

Project number: {{ cookiecutter.project_number }}.

TODO: add the documentation of your code here, what the aim is, etc.


## Prefect flow development

Some `uv` commands:

    $ uv sync  # Sets up the .venv and does the "pip install"
    $ uv add your-dependency  # If you need numpy or so; replaces requirements.txt
    $ uv run prefect server start  # "uv run" automatically runs in your .venv
    $ uv run src/tasks.py

Write your script in the `src` folder, with your 'main' script in `flows.py`, and tasks
in `tasks.py`. Feel free to add new folders or files in the `src` folder. Create a
deployment in `python src/server.py`.

- To test your flow locally, start a prefect instance within your venv:

        $ uv run prefect server start

- Run `uv run src/flows.py` to run your script, or `uv run src/server.py` to test the deployment.


## Code neatness

Install the pre-commit for this git repo:

    $ pre-commit install

This runs pre-commit on every commit, making sure everything is neat. Github also runs it as a sort of test, to make sure no preventable errors end up in the generated docker image. If you have troubles with pre-commit, you can always run it manually with:

    $ pre-commit run --all


## Deploying your flow to production

Ask Taj or Reinout to add your new flow to the [prefect-setup repo](https://github.com/nens/prefect-setup/blob/main/docker-compose.task.yml)_.

On every commit to the `main` branch, a new docker image is generated on github *if pre-commit doesn't complain*. The prefect-setup docker-compose looks for new images every five minutes and downloads+restarts when available.


## Optional (but definitely recommended):

If you use vscode and did the `.venv` thingy above, the python plugin will detect your code and prefect. So you'll have proper code completion! And type hints become more useful. Tip: also install [the vscode editorconfig plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) because that will automatically handle unneeded spaces at the end of lines and other minutia.
