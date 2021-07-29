# Postmark FastAPI

The aim of this repository is to show a demo of [Postmark](https://postmarkapp.com/) as an inbound email provider using [FastAPI](https://fastapi.tiangolo.com/) as a web service to provide a webhook.

## Running API

This repository uses [Pipenv](https://pipenv.pypa.io/en/latest/install/).

Once you have pipenv installed, run`pipenv install`.

- Run `pipenv shell`
- Run `uvicorn main:app --reload`

In order to expose the webhook to the web, you can use [ngrok](https://ngrok.com/). Once you have installed ngrok, you can run `ngrok http http://127.0.0.1:8000/`.

## Setting up postmark

- In Postmark create a mail server
- Go to the "Inbound Stream"
- Set the webhook URI to be a your ngrok url e.g. https://xxxxx.ngrok.io/inbound
- Send an email to your postmark address e.g. xxxx@inbound.postmarkapp.com
