from prefect import flow
from tasks import uppercase_the_text


# Note: prefix the flows with "the_project_name_", that's the only way to prevent a
# total unclear mess in the prefect user interface :-)
@flow(log_prints=True)
def {{ cookiecutter.__underscore_name }}_example_flow(text: str = "Hi"):
    uppercase_text = uppercase_the_text(text)
    print(f"Turned {text} into {uppercase_text}")


if __name__ == "__main__":
    print("Not serving flows, but running them locally for testing")
    {{ cookiecutter.__underscore_name }}_example_flow()
