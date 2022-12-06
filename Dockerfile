FROM python:3.8-slim
ARG port

USER root
COPY . /myApp
WORKDIR /myApp

ENV PORT=$port

RUN pip freeze > requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /myApp \
    && chmod -R g=u /myApp \
    && pip install pip --upgrade \
    && pip install -r requirements.txt
EXPOSE $PORT

CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload
