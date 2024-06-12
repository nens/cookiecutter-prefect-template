# Cookiecutter template for N&S prefect projects

Cookiecutter ([www.cookiecutter.io](https://www.cookiecutter.io/)) generates fresh projects from a template. `cookiecutter-prefect-template` is the template for our prefect tasks/flows. The advantage: easy to start and a similar structure for every project.

## Using the cookiecutter

You need to install the cookiecutter program with pip (or pipx). Then you can call it with the URL of this template's github repo.

    $ pip install "cookiecutter"
    $ cookiecutter --version  # Should be 2 or higher.
    $ cookiecutter https://github.com/nens/cookiecutter-prefect-template

It will ask for a project name:

- Lowercase only, please.
- Start with `prefect-`.
- Dashes, no underscores.
- So something like `prefect-flater-sync`.

Create a new repo on github **with exactly the same name**. Make it an empty repo, so don't let github generate a license or readme. If you do generate a readme, you'll have to copy over generated files by hand and you'll probably forget the hidden `.github/` files and so, so don't do that :-)

Instructions for the paragraph above will be printed after generating the project, but mentioning it twice won't hurt.


## Development on this template

The regular:

    $ uv venv
    $ source .venv/bin/activate
    $ uv pip install -r requirements.txt


## Short explanation of the server setup

Prefect can be run in multiple ways. Often, the cloud offering is used. We host our own server.

More interesting for this template is how we run the flows+tasks. A common way is to have some task server ("agent", I believe) ready to run dockers or download code or execute locally installed code.

An alternative is to call `.serve()` on a deployment, like we do in the code generated with this template. The code you're working on will then "register" itself with the server and will keep a connection open, waiting for instructions to run.

We run it ourselves with docker-compose at the moment. Every project generated with the template has a github workflow that builds a docker image. The docker-compose lists all those images. A `prefect.env` environment file with just the `PREFECT_API_URL` env variable is given to the docker (or a different env file with more settings).

And as an extra, we use the [containrrr/watchtower](https://containrrr.dev/watchtower/) docker that looks every five minutes whether there's a new image for any of the containers and if true, downloads it and restarts the service. Handy mechanism for allowing colleagues to update their docker images without actually having to log in to the server.

Here's an example docker-compose file:

```
services:

  # Watchtower checks for new containers every five minutes and updates them
  # when available.
  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - $HOME/.docker/config.json:/config.json
    restart: unless-stopped
    command: --interval 300 --include-restarting --include-stopped --revive-stopped

  prefect-some-thing:
    image: ghcr.io/nens/prefect-some-thing:main
    env_file:
      - prefect.env
    restart: unless-stopped

  prefect-something-else:
    image: ghcr.io/nens/prefect-something-else:main
    env_file:
      - prefect.env
    restart: unless-stopped

  prefect-tema-demo:
    image: ghcr.io/nens/prefect-tema-demo:main
    env_file:
      - tema-demo.env
    restart: unless-stopped
```
