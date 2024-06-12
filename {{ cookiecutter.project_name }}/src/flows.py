from prefect import flow
from tasks import uppercase_the_text


@flow(
    name="{{ cookiecutter.__underscore_name }} Flow",
    flow_run_name = "{{ cookiecutter.__underscore_name }} Flow run",
    description= "Short description of what the flow does.",
    retries=0, # If wanted, place your retries count here,
    retry_delay_seconds=10,
    log_prints=True
)
def {{ cookiecutter.__underscore_name }}_flow(text: str = "Hi"):
    uppercase_text = uppercase_the_text(text)
    print(f"Turned {text} into {uppercase_text}")


if __name__ == "__main__":
    print("Not serving flows, but running them locally for testing")
    {{ cookiecutter.__underscore_name }}_flow()
