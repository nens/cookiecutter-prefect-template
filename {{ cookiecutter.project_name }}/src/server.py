from flows import {{ cookiecutter.__underscore_name }}_example_flow
from prefect import serve

if __name__ == "__main__":

    deploy1 = {{ cookiecutter.__underscore_name }}_example_flow.to_deployment(
        name="{{ cookiecutter.__underscore_name }}_test-deploy",
        interval=60,
        parameters={"text": "Python is absolutely fabulous"},
    )
    # deploy2 = ...

    serve(deploy1)  # serve(deploy1, deploy2)
