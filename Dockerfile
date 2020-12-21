FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /code/
# Import default data set
RUN python -m dlmsearch --import-csv ./data/default.csv
ENTRYPOINT gunicorn dlmsearch.app:app --bind='0.0.0.0:8000'
