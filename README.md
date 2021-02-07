# python-config

This repo demonstrates a lightweight python config suitable for multi-stage deployments in a serverless environment.

## Requirements

    python version: 3.8

## Development

1. Install pipenv: `pip install pipenv`
2. Build the environment: `pipenv --python 3.8`
3. Install dependencies (including dev dependencies): `pipenv install --dev`

#### Notes on pipenv

Make sure to set `PIPENV_VENV_IN_PROJECT`, e.g. in your `~/.zshrc` or `~/.bash_profile` via `export PIPENV_VENV_IN_PROJECT=true`. This allows VSCode to detect the correct virtualenv, as `pipenv` will put it into `.venv` in the workspace folder.

- If you need to enter a subshell where the the virtual env is activated, use: `pipenv shell`
- During development, use pipenv to manage dependencies:
    - `pipenv install --dev some-package #install only for dev`
    - `pipenv install some-package #install for prod`
- If something goes wrong in your pipenv, `CTRL-d` out of the venv subshell (if active), then nuke the venv via `pipenv --rm` and rebuild it (see above).

