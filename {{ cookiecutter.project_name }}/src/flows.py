from prefect import flow

from tasks import uppercase_the_text


@flow(
    name="Clear name of your flow",
    flow_run_name="{{ cookiecutter.__underscore_name }} Flow run",
    description="Short description of what the flow does.",
    retries=0,  # If wanted, place your retries count here,
    retry_delay_seconds=10,
    log_prints=True,
)
def {{ cookiecutter.__underscore_name }}_flow(text: str = "Hi"):
    uppercase_text = uppercase_the_text(text)
    print(f"Turned {text} into {uppercase_text}")


if __name__ == "__main__":
    # This __main__ isn't used on the server, so you can use it for local development.
    # In vscode, run it with "{{ cookiecutter.__debug_action_name }}" (with a temp
    # prefect server) or start a prefect server in the terminal with:
    #
    # $ uv run prefect server start
    #
    # And then run it with "{{ cookiecutter.__localhost_debug_action_name }}".
    # The output is shown in the "debug console".
    print("Not serving flows, but running them locally for testing")
    {{ cookiecutter.__underscore_name }}_flow()
