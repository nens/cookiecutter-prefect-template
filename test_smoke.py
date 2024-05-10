import sys
from contextlib import chdir
from pathlib import Path
from subprocess import run

import pytest
from cookiecutter.main import cookiecutter


def test_smoke(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={"project_name": "prefect-my-example", "project_number": "R1972"},
        no_input=True,
    )


def test_function_prefix(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={
            "project_name": "prefect-nens-customer",
            "project_number": "R1972",
        },
        no_input=True,
    )
    generated_flows_py = tmp_path / "prefect-nens-customer/src/flows.py"
    # We prefix everything with our project name, but want to omit the prefect part.
    print(generated_flows_py.read_text())  # For easier debugging
    assert "def nens_customer_example_flow" in generated_flows_py.read_text()


def test_generated_project(tmp_path: Path):
    if sys.platform.startswith("win"):
        pytest.skip("Skipping test that uses linux commands")
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={"project_name": "prefect-my-example", "project_number": "R1972"},
        no_input=True,
    )
    with chdir(tmp_path / "prefect-my-example"):
        run(["git", "init"], check=True)
        run(["git", "add", "-A"], check=True)
        run([sys.executable, "-m", "venv", ".venv"], check=True)
        run([".venv/bin/pip", "install", "-r", "requirements.txt"], check=True)
        run([".venv/bin/pip", "install", "pre-commit"], check=True)
        run([".venv/bin/pre-commit", "run", "--all"], check=True)
        run([".venv/bin/pytest"], check=True)
