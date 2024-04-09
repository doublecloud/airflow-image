# DoubleCloud Airflow base container images

## Container images

Runtime container images used for DoubleCloud Airflow clusters are available in the [GitHub Container registry](https://github.com/doublecloud/airflow-image/pkgs/container/airflow).

Each published image has two tags:

1. "Floating" or movable tag, such as `2.8.1`, that points to the latest build of an image related to the Airflow version
2. Fixed tag, such as `2.8.1-1`, that points to the specific build of an image related to the Airflow version

You can find the installed Python packages and changelogs in directories inside the `versions` directory.
