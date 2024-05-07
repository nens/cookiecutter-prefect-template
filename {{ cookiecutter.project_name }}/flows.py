from prefect import flow, task


@task(retries=2)
def uppercase_the_text(text: str) -> str:
    """Return uppercased text"""
    return text.upper()


@flow(log_prints=True)
def example_flow(text: str = "Hi"):
    uppercase_text = uppercase_the_text(text)
    print(f"Turned {text} into {uppercase_text}")


if __name__ == "__main__":
    print("Not serving flows, but running them locally for testing")
    example_flow()
