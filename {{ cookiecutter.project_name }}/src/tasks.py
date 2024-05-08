from prefect import task


@task(retries=2)
def uppercase_the_text(text: str) -> str:
    """Return uppercased text"""
    return text.upper()
