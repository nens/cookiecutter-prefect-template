from pathlib import Path

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_NUMBER = "{{ cookiecutter.project_number }}"


def print_instructions(
    project_name: str = PROJECT_NAME, project_number: str = PROJECT_NUMBER
):
    # This hook is executed inside the generated directory.
    current_dir = str(Path(".").absolute())

    base_url = "https://github.com/new?"
    arguments = [
        f"name={project_name}",
        "owner=nens",
        "visibility=private",
        f"description=Prefect+tasks+for+{project_number}",
    ]
    creation_url = base_url + "&".join(arguments)
    print("First, use the following url to a new empty repo on github.")
    print("'Empty' means don't let github generate a readme, .gitignore or license:")
    print("the cookiecutter already has them ready for you.")
    print("")
    print(creation_url)
    print("")
    print("Done?")
    print("")
    print("Then go to the generated project and do some git magic:")
    print("")

    print(f"cd {current_dir}")
    print("git init")
    print("git add -A")
    print('git commit -m "Generated with cookiecutter"')
    print("git branch -M main")
    print(f"git remote add origin git@github.com:nens/{project_name}.git")
    print("git push origin")
    print(" ")


if __name__ == "__main__":
    print_instructions()
