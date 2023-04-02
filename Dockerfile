FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code
RUN pip install -U pip
RUN pip install -e .
# Import default data set
RUN python -m dlmsearch --import-csv ./data/default.csv
ENTRYPOINT gunicorn dlmsearch --bind='0.0.0.0:8000'
