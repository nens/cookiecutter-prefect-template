import pytest

from hooks.post_gen_project import print_instructions
from hooks.pre_gen_project import validate_project_name


def test_valid_name():
    # Just returns None, it doesn't do a sys.exit(1)
    validate_project_name("prefect-reinout-test")


@pytest.mark.parametrize("name", ["Uppercase", "under_scores", "no-prefect-prefix"])
def test_invalid_name(name: str):
    with pytest.raises(SystemExit):
        validate_project_name(name)


def test_print_instructions():
    print_instructions(project_name="prefect-example-project")
