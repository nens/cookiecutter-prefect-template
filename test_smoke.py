from pathlib import Path

from cookiecutter.main import cookiecutter


def test_smoke(tmp_path: Path):
    cookiecutter(
        template=".",
        output_dir=str(tmp_path),
        extra_context={"project_name": "my-example", "project_number": "R1972"},
        no_input=True,
    )
