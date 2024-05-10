# This hook is run after the questions, before the template process. See
# https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html
import sys

project_name = "{{ cookiecutter.project_name }}"


def validate_project_name(name: str = project_name):
    # Exit if the namne is not correct.
    if name != name.lower():
        print("Convention: project_name should be all-lowercase")
        sys.exit(1)
    if "_" in name:
        print("Convention: project_name should use - instead of underscores")
        sys.exit(1)
    if not name.startswith("prefect-"):
        print("Convention: project_name should start with 'prefect-'")
        sys.exit(1)


if __name__ == "__main__":
    validate_project_name()
