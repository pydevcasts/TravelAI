FROM python:3.11.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
USER root

ENV HOME=/code
ENV APP_HOME=/code

RUN mkdir $APP_HOME
RUN mkdir -p /code/media/static

WORKDIR $APP_HOME

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r ./requirements.txt

COPY . $APP_HOME

EXPOSE 8000

CMD ["gunicorn", "app:app", "--workers", "3", "--worker-class", "sync", "--bind", "0.0.0.0:8000"]