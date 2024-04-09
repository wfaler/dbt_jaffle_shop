SHELL := /bin/bash


.PHONY: deploy
deploy:
	mkdir -p dags/dbt/seeds
	mkdir -p dags/dbt/models
	mkdir -p dags/dbt/target
	cp -r seeds/* dags/dbt/seeds/
	cp -r models/* dags/dbt/models/
	cp dbt_project.yml dags/dbt/
	cp profiles.yml dags/dbt/
	cp dbt_airflow_dag.py dags/

.PHONY: run
run:
	poetry run dbt run

.PHONY: test
test:
	poetry run dbt test
