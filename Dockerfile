# # Build base docker image with pipenv
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 AS unicorn-pipenv

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# Build app
FROM unicorn-pipenv

COPY ./app /app

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
