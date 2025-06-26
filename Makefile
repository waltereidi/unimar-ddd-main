build:
	docker compose build
run:
	docker compose up -d
stop:
	docker compose stop
bash:
	docker compose exec -it unimar-ddd-main-postgres-1 bash
runserver:
	docker compose run biblioteca-api