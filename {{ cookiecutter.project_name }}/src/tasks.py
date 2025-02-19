# When using vscode, you can set a breakpoint somewhere in a task to inspect it in
# detail. Then run the debugger on flows.py. Make sure the task you want to debug is
# actually called in flows.py, of course :-)
from prefect import task


@task(retries=2)
def uppercase_the_text(text: str) -> str:
    """Return uppercased text"""
    return text.upper()
