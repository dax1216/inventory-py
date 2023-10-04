FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install --no-install-recommends -y build-essential

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app

CMD gunicorn itdept.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
