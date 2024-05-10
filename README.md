# Cookiecutter template for N&S prefect projects

Cookiecutter ([www.cookiecutter.io](https://www.cookiecutter.io/)) generates fresh projects from a template. `cookiecutter-prefect-template` is the template for our prefect tasks/flows. The advantage: easy to start and a similar structure for every project.

## Using the cookiecutter

You need to install the cookiecutter program with pip (or pipx). Then you can call it with the URL of this template's github repo.

    $ pip install "cookiecutter"
    $ cookiecutter --version  # Should be 2 or higher.
    $ cookiecutter https://github.com/nens/cookiecutter-prefect-template

It will ask for a project name:

- Lowercase only, please.
- Start with `prefect-`.
- Dashes, no underscores.
- So something like `prefect-flater-sync`.

Create a new repo on github **with exactly the same name**. Make it an empty repo, so don't let github generate a license or readme. If you do generate a readme, you'll have to copy over generated files by hand and you'll probably forget the hidden `.github/` files and so, so don't do that :-)

Instructions for the paragraph above will be printed after generating the project, but mentioning it twice won't hurt.


## Development on this template

The regular:

    $ uv venv
    $ source .venv/bin/activate
    $ uv pip install -r requirements.txt
