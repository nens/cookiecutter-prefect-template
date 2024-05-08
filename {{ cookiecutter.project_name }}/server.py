import os

from prefect import serve

from flows import example_flow

if __name__ == "__main__":
    assert "PREFECT_API_URL" in os.environ
    print(f"Serving flows for {os.environ['PREFECT_API_URL']}")

    deploy1 = example_flow.to_deployment(
        name="test-deploy",
        interval=60,
        parameters={"text": "Python is absolutely fabulous"},
    )
    # deploy2 = ...

    serve(deploy1)  # serve(deploy1, deploy2)
