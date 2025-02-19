# When using vscode, you can set a breakpoint somewhere in a task to inspect it in
# detail. Then run the debugger with {{ cookiecutter.__debug_action_name }}
# selected, this runs flows.py using localhost:4200.
#
# - Make sure the task you want to debug is actually called in flows.py, of course :-)
# - Start prefect as explained in flows.py.

from prefect import task


@task(retries=2)
def uppercase_the_text(text: str) -> str:
    """Return uppercased text"""
    return text.upper()
