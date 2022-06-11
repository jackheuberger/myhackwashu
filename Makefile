
run: reset-data
	. ./app.env; . ./db.env; ./env/bin/python manage.py runserver 0.0.0.0:8000
	
reset-data:
	docker-compose down
	docker volume remove myhackwashu_data