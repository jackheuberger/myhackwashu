.DEFAULT_GOAL := list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

local: create-env reset-data db-container
	bash restart.sh
	. ./app.env; . ./db-local.env; ./env/bin/python manage.py runserver 0.0.0.0:8000

compose: reset-data
	docker-compose up --build

create-env:
	virtualenv env --python=python3
	
reset-data:
	docker-compose down || true
	docker volume remove myhackwashu_data || true

db-container:
	docker-compose up -d db 
	
.PHONY: db-container reset-data create-env compose local list
