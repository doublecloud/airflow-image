ARG AIRFLOW_TAG
FROM apache/airflow:${AIRFLOW_TAG}
COPY versions/${AIRFLOW_VERSION}/requirements.txt /requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
