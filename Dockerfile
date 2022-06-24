FROM apache/airflow:2.2.3-python3.8
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


USER airflow

COPY ./requirements.txt ./requirements.txt

COPY ./dags /opt/airflow/dags
COPY ./rhino /opt/airflow/plugins/rhino/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \


