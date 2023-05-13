FROM python:3.10-slim

RUN apt-get clean && apt-get update

RUN apt-get install -qy nano

WORKDIR /yamdb_final

COPY api_yamdb/requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./ ./

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
