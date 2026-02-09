# This hook is run after the questions, before the template process. See
# https://cookiecutter.readthedocs.io/en/stable/advanced/hooks.html
import sys

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PREFECT_VERSION = "{{ cookiecutter.prefect_version }}"


def validate_project_name(project_name: str = PROJECT_NAME):
    # Exit if the namne is not correct.
    if project_name != project_name.lower():
        print("ERROR: Convention - project_name should be all-lowercase")
        sys.exit(1)
    if "_" in project_name:
        print("ERROR: Convention - project_name should use - instead of underscores")
        sys.exit(1)
    if not project_name.startswith("prefect-"):
        print("ERROR: Convention - project_name should start with 'prefect-'")
        sys.exit(1)

def validate_prefect_verion(prefect_version: str = PREFECT_VERSION):
    # Exit if prefect version is not 2 or 3
    if prefect_version not in ["2", "3"]:
        print("ERROR: Prefect version must be either 2 or 3")
        sys.exit(1)        


if __name__ == "__main__":
    validate_project_name()
    validate_prefect_verion()
