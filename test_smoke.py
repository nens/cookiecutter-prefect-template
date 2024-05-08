import sys
from contextlib import chdir
from pathlib import Path
from subprocess import run

from cookiecutter.main import cookiecutter


def test_smoke(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={"project_name": "my-example", "project_number": "R1972"},
        no_input=True,
    )


# TODO: skip this test on windows as it won't work.
def test_generated_project(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={"project_name": "my-example", "project_number": "R1972"},
        no_input=True,
    )
    with chdir(tmp_path / "my-example"):
        run([sys.executable, "-m", "venv", ".venv"], check=True)
        run([".venv/bin/pip", "install", "-r", "requirements.txt"], check=True)
        run([".venv/bin/pip", "install", "pre-commit"], check=True)
        run(["git", "init"], check=True)
        run([".venv/bin/pre-commit", "run", "--all"], check=True)
        run([".venv/bin/pytest"], check=True)
