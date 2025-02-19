# {{ cookiecutter.project_name }} prefect task

## Post-generation checklist

First a little bit of github administration:

- [ ] Just making sure: you created a github repo and did the init/add/push shown after generating the project?
- [ ] Go to the ["manage access" page](https://github.com/nens/{{ cookiecutter.project_name }}/settings/access) and click "add teams": add the "adviseurs" team with **write** access. Otherwise you're the only one who can work on it.
- [ ] On that same page, add the team "nelen-schuurmans-pull-only" with **read** access. Otherwise the server cannot download the docker image.

If you're working on other prefect tasks, you probably have these two installed already:

- [ ] Instead of virtualenv&pip, we now use `uv`. It handles the virtualenv, the pip install, pinning versions. It also works much faster. You need to install it, [here are the instructions](https://docs.astral.sh/uv/getting-started/installation/).
- [ ] To keep the code readable and maintainable, we use pre-commit. Install it with `pip install pre-commit` .
- [ ] Set up pre-commit to automatically run before every commit: `pre-commit install` .

Lastly a bit of readme cleanup:

- [ ] In the next section, quickly add an initial sentence about the project.
- [ ] Remove this whole post-generation checklist from the readme. You won't need it anymore as you've diligently checked off every item :-)


## Project documentation

Project number: {{ cookiecutter.project_number }}.

TODO: add the documentation of your code here, what the aim is, etc.


## Development instructions

Some `uv` commands:

    $ uv sync  # Sets up the .venv and does the "pip install"
    $ uv add your-dependency  # If you need numpy or so; replaces requirements.txt
    $ uv run prefect server start  # "uv run" automatically runs in your .venv
    $ uv run src/flows.py
    $ uv sync --upgrade  # Allow upgrades to versions.

Write your script in the `src` folder, with your 'main' script in `flows.py`, and tasks
in `tasks.py`. Feel free to add new folders or files in the `src` folder. Create a
deployment in `python src/server.py`.

There are test instructions in `flows.py` and `tasks.py`. Running `flows.py` will start a temporary prefect server and run whatever tasks you call in the `__main__`:

    $ uv run src/flows.py


## Handy vscode setup: all ready for use

- If you use vscode and did the `uv sync` thingy above, the python plugin will detect   your code and prefect. So you'll have proper code completion! And type hints become more useful.
- Vscode will **recommend** "python", "editorconfig" and "ruff" extensions: install them. Vscode will ask about trusting "editorconfig" and "astral software": yes, that's okay. - Editorconfig handles unneeded spaces at the end of lines and other minutia.
- Ruff formats your code and sorts the imports whenever you save a file. It will also warn about unknown variables or unused imports and offer fixes.
- The "run and debug" button in the activity bar runs `src/flows.py` against localhost:4200 if you select "{{ cookiecutter.__debug_action_name }}" in the dropdown. See the instructions in `src/flows.py` on how to use it.

Nice, easy, modern development with mostly-automatic formatting and neatness!


## Deploying your flow to production

On every commit to the `main` branch, a new docker image is generated on github *if pre-commit doesn't complain* and *if the docker image can be build*. The server looks for new images every five minutes and downloads+restarts it automatically.

Should the github action complain about pre-commit, upgrade the config and run it again:

    $ pre-commit autoupdate
    $ pre-commit run --all

Should the github action fail on the docker image creation, try that one out locally and fix any errors:

    $ docker build .

Initially, ask Taj or Reinout to add your new deployment to the [prefect-setup repo](https://github.com/nens/prefect-setup/blob/main/docker-compose.task.yml)_.
