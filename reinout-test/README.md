# reinout-test prefect task


## Post-generation steps

- Ask Reinout to adjust the github permissions for the project.



## Local development

TODO

## Running it on the server... happens automatically

It happens automatically after some one-time configuring:

- Github builds a new docker image for `main`.
- https://github.com/nens/prefect-setup has a `docker-compose.task.yml` that reloads new versions of the docker image and passes the `PREFECT_API_URL` environment variable.
- That docker runs your `server.py` with your configured deployments.
