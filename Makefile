db-upgrade:
	@docker-compose up -d db
	@sleep 5
	@docker-compose run web python manage.py migrate
run:
	@docker-compose up  --remove-orphans
stop:
	@docker-compose down --remove-orphans