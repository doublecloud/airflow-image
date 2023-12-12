ARG AIRFLOW_TAG
FROM apache/airflow:${AIRFLOW_TAG}
ARG BUILD_LABEL
USER airflow
COPY versions/${AIRFLOW_VERSION}/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
LABEL cloud.double.airflow.image-version=${BUILD_LABEL}
