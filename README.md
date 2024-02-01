# DoubleCloud Airflow Base Docker Images

## Docker images

Docker images being used as runtime on DoubleCloud Airflow clusters are currently available at [GitHub Container Registry](https://github.com/doublecloud/airflow-image/pkgs/container/airflow).

Each published image has two tags:
1. "Floating" or movable tag like `2.8.1` that points at the latest build of an image related to the Airflow version
2. Fixed tags like `2.8.1-1` that points at the specific build of an image related to the Airflow version

You can find installed python packages and changelogs in version directories inside `versions` directory.
