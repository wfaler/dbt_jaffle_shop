FROM apache/airflow:2.8.3-python3.11
RUN pip install dbt-core dbt-postgres
