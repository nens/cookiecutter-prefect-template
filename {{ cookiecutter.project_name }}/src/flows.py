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
    # In vscode, start a prefect server in the terminal with:
    #
    # $ uv run prefect server start
    #
    # And then run the vscode debugger with "{{ cookiecutter.__debug_action_name }}"
    # selected. This runs flows.py, so whatever is below here gets called. Set
    # breakpoints in tasks.py as needed.
    # The output is shown in the "debug console".
    print("Not serving flows, but running them locally for testing")
    {{ cookiecutter.__underscore_name }}_flow()
