# fastapi-template

A repository to setup cleann fastapi template for setting up your APIs with modular components.

## Virtual Environment

```
python -m venv env
source ./env/bin/activate
```

## Setup Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

```
pip install poetry
poetry new app
poetry install
pytest
```

## Install FastAPI and ASGI Server

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

```
poetry add fastapi
poetry add "uvicorn[standard]"
```

[standard] will install uvicorn with minimal (pure Python) dependencies.

## Run the application

```
uvicorn app.main:app --reload
```
