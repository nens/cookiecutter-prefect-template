import os

from dotenv import load_dotenv
from flows import main
from prefect import serve

load_dotenv()

if __name__ == "__main__":
    assert "PREFECT_API_URL" in os.environ
    print(f"Serving flows for {os.environ['PREFECT_API_URL']}")

    deploy1 = main.to_deployment(
        name="test-deploy",
        interval=60,
        parameters={"text": "Python is absolutely fabulous"},
    )
    # deploy2 = ...

    serve(deploy1)  # serve(deploy1, deploy2)
