from flows import {{ cookiecutter.__underscore_name }}_flow
from prefect import serve

if __name__ == "__main__":

    {{ cookiecutter.__underscore_name }}_deployment = {{ cookiecutter.__underscore_name }}_flow.to_deployment(
        name="Clear name of your deployment",
        interval=60, # alternative: cron="5 4 * * *". Check crontab.guru to create the correct schedule expression
        parameters={"text": "Python is absolutely fabulous"}, # Input needs to be convertable to json
        description="Code found at: https://github.com/nens/{{ project_name }}", # Place this in EACH deployment, so that it its clear which repo serves which deployment
        tags=["Your name", "Project keyword"] # Add the name of the first point of contact, and one or more keywords of the project
    )


    serve({{ cookiecutter.__underscore_name }}_deployment)  # It is possible to create multiple deployments and serve them all.
