DOCKER_COMPOSE:=docker compose
DOCKER_COMPOSE_YML:=--file docker-compose.yml
SUCCESS_MESSAGE:="Base app is running on http://localhost:3000!" 

# Docker's container names based on the compose file
APP_CONTAINER:=runserver
POSTGRES:=postgres
APP_IMAGE:=budget_web_app_api

# Docker's Service names
APP_SERVICE_NAME:=api
POSTGRES_SERVICE_NAME := db

# Edit these! Update with your own values
ENV_FILE_LOCATION:=.env.dev
POSTGRES_USER:=postgres
CONTAINER_MANAGE_LOCATION:=src


.PHONY: up
up:
	@$(DOCKER_COMPOSE) \
		$(DOCKER_COMPOSE_YML) \
		--env-file $(ENV_FILE_LOCATION) \
		$@ --build --detach
	@echo $(SUCCESS_MESSAGE)
		

.PHONY: stop
stop:
	@$(DOCKER_COMPOSE) stop $(APP_SERVICE_NAME) $(POSTGRES_SERVICE_NAME)


.PHONY: runserver
runserver:
	@$(DOCKER_COMPOSE) start $(APP_SERVICE_NAME) $(POSTGRES_SERVICE_NAME)
		

.PHONY: teardown
IMAGES?=
teardown:
	@$(DOCKER_COMPOSE) down --volumes
	@if [ "$(IMAGES)" = "true" ]; then \
		docker image rm $(POSTGRES) $(APP_IMAGE); \
	fi

	

.PHONY: bash
bash:
	@docker exec -it $(APP_CONTAINER) bash


.PHONY: shell
shell:
	@docker exec -it $(APP_CONTAINER) python3 src/manage.py shell_plus --ipython


.PHONY: dbshell
dbshell:
	@docker exec -it $(POSTGRES) psql -U $(POSTGRES_USER)


.PHONY: makemigrations
makemigrations: 
	@docker exec -it $(APP_CONTAINER) python $(CONTAINER_MANAGE_LOCATION)/manage.py $@


.PHONY: migrate
migrate:
	@docker exec -it $(APP_CONTAINER) python $(CONTAINER_MANAGE_LOCATION)/manage.py $@


.PHONY: startapp
APP?=
startapp:
	@if [ -z $(APP) ]; then \
		echo "No app was specified. Please retry with an app name."; \
	else \
		docker exec $(APP_CONTAINER) python3 src/manage.py startapp $(APP); \
	fi


.PHONY: help
help:
	@echo " -																															"
	@echo " General targets:																											"
	@echo "		up			Build the service image, create the service and db container, create the network and connect the containers."
	@echo "		start			Start up the existing service and database containers.													"
	@echo "		stop			Stop the running service and database containers.														"
	@echo "		teardown		Stop and remove the service and database containers and remove the relative network and volumes.		"
	@echo "		makemigrations		Create migrations for the service.																	"
	@echo "		migrate			Run migrations for the service.																			"
	@echo "		startapp		Create a Django app.																					"
	@echo " -																															"
	@echo " -																															"
	@echo " Docker development																											"
	@echo "		shell			Start a shell_plus session.																				"
	@echo "		dbshell			Start an dbshell session for the Postgres database.														"
	@echo "		bash			Start a bash session.																					"
	@echo " -																															"


include make-utils/base-builds.mk 