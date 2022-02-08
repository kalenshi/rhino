FROM apache/airflow:2.2.3-python3.8
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

USER root

RUN set -ex \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev

USER airflow

COPY ./requirements.txt ./requirements.txt

COPY ./dags /opt/airflow/dags
COPY ./rhino /opt/airflow/plugins/rhino/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

