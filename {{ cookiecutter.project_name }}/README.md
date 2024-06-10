# {{ cookiecutter.project_name }} prefect task

## Project Documentation

#TODO: add the documentation of your code here

## Prefect flow development

- Create a virtual environment and install the requirements.txt:

        $ python3 -m venv .venv            # Only needed once
        $ .venv\Scripts\activate           # Activate on windows
        $ source .venv/bin/activate        # Activate on linux
        $ pip install -r requirements.txt  # Whenever requirements.txt changes

- Write your script in the `src` folder, with your 'main' script in `flows.py`, and tasks in `tasks.py`. Feel free to add new folders or files in the `src` folder.

- Create a deployment in `python src/server.py`.

- To test your flow locally, start a prefect instance within your venv:

        $ prefect server start

- Run `python src/flows.py` to run your script, or `python src/server.py` to test the deployment.

## Deploying your flow to production

- Create a repo on the nens github with the EXACT same name as your repo. It should start with 'prefect-'.

- Start a local git project:

        $ git init

- To keep code readable and maintainable, pre-commit is installed. If you have never used it, install globally on your device with:

        $ pip install pre-commit

- Install the pre-commit for this git repo:

        $ pre-commit install

- Commit your code and push it to your new repo. If you have troubles with pre-commit, you can always run it manually with:

        $ pre-commit run --all

> **_NOTE:_**  You need to fix all the pre-commit problems if it doesn't fix them itself. If pre-commit fails, the docker image build will also fail, and your flow will not be deployed.

- Add 2 new teams to your github repo: Adviseurs (write) and Nelen & Schuurmans pull only (admin)

- Ask Florian or Reinout to register your new flow.


## Optional (but definitely recommended):

If you use vscode and did the `.venv` thingy above, the python plugin will detect your code and prefect. So you'll have proper code completion! And type hints become more useful. Tip: also install [the vscode editorconfig plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) because that will automatically handle unneeded spaces at the end of lines and other minutia.

There are even tests files (see https://docs.pytest.org/ for instructions), you can use them to test calculations. Ask Reinout or Florian for tips. Don't test whether an ftp download can work, but *do* test when you do some real programming work.

Once the virtualenv is activated, you can run the tests simply with:

        $ pytest
