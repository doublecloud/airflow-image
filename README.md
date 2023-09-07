# DoubleCloud Airflow Base Docker Images

## Docker images

Docker images that are used for operation of DoubleCloud Airflow clusters are currently available on [GitHub Container Registry](https://github.com/doublecloud/airflow-image/pkgs/container/airflow).

We tag every published image with two tags:
1. "Floating" or movable tag like `2.6.3` that points at the latest build of an image related to the Airflow version
2. Fixed tags like `2.6.3-2` that points at the specific build of an image related to the Airflow version

You can find installed python packages and changelogs in version directories inside `versions` directory.
