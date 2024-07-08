from pathlib import Path

PROJECT_NAME = "{{ cookiecutter.project_name }}"


def print_instructions(project_name: str = PROJECT_NAME):
    # This hook is executed inside the generated directory.
    current_dir = str(Path(".").absolute())

    print("Go to https://github.com/orgs/nens/repositories and create a new empty repo")
    print(f"called '{project_name}'. 'Empty' means don't let github generate a readme")
    print("or a .gitignore, the cookiecutter already has them ready for you.")
    print("")
    print("Done?")
    print("")
    print("Then go to the generated project and do some git magic:")
    print("")

    print(f"cd {current_dir}")
    print("git init")
    print("git add -A")
    print('git commit -m "Generated with cookiecutter"')
    print('git branch -M main')
    print(f"git remote add origin git@github.com:nens/{project_name}.git")
    print("git push origin")
    print(" ")


if __name__ == "__main__":
    print_instructions()
