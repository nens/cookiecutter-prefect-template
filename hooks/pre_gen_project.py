# This hook is run after the questions, before the template process. See
# https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html
import sys

PROJECT_NAME = "{{ cookiecutter.project_name }}"


def validate_project_name(project_name: str = PROJECT_NAME):
    # Exit if the namne is not correct.
    if project_name != project_name.lower():
        print("Convention: project_name should be all-lowercase")
        sys.exit(1)
    if "_" in project_name:
        print("Convention: project_name should use - instead of underscores")
        sys.exit(1)
    if not project_name.startswith("prefect-"):
        print("Convention: project_name should start with 'prefect-'")
        sys.exit(1)


if __name__ == "__main__":
    validate_project_name()
