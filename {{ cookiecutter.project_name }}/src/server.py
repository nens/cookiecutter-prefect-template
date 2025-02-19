from prefect import serve

from flows import {{ cookiecutter.__underscore_name }}_flow

if __name__ == "__main__":
    # This __main__ is called in the dockerfile to actually serve your flows. You can
    # test the setup here by running prefect locally and calling this file with the
    # PREFECT_API_URL environment variable set to your locally running prefect.
    # The main testing/tweaking during development will be in flows.py and tasks.py.

    {{ cookiecutter.__underscore_name }}_deployment = {{ cookiecutter.__underscore_name }}_flow.to_deployment(
        name="Clear name of your deployment",
        interval=60,
        # ^^^ alternative: cron="5 4 * * *". Check crontab.guru to create the correct
        # schedule expression.
        parameters={"text": "Python is absolutely fabulous"},
        # ^^^ Input needs to be convertable to json.
        description="Code found at: https://github.com/nens/{{ cookiecutter.project_name }}",
        # ^^^ Place this in EACH deployment, so that it its clear which repo serves which deployment.
        tags=["Your name", "Project keyword"],
        # ^^^ Add the name of the first point of contact, and one or more keywords of the project.
    )

    serve({{ cookiecutter.__underscore_name }}_deployment)
    # It is possible to create multiple deployments and serve them all, just pass them like:
    # serve(
    #     {{ cookiecutter.__underscore_name }}_deployment1,
    #     {{ cookiecutter.__underscore_name }}_deployment2,
    #     {{ cookiecutter.__underscore_name }}_deployment3
    # )
