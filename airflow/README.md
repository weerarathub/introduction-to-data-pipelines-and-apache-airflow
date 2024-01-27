Workspace
Running Airflow in Docker
Before we run Airflow, let's create these folders below first. Please note that if you're using Windows, you can skip this step.

mkdir -p mnt/dags mnt/logs mnt/plugins mnt/tests
On Linux, please make sure to configure the Airflow user for the docker-compose:

echo -e "AIRFLOW_UID=$(id -u)" > .env
docker compose build
docker compose up
To stop Airflow, run:

docker compose down