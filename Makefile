DOCKER_COMPOSE := docker-compose
DOCKER_COMPOSE_YML := --file docker-compose.yml
SUCCESS_MESSAGE := "Base app is running on http://localhost:3000!" 

# Docker's container names based on the compose file
APP_CONTAINER := runserver
POSTGRES_CONTAINER := postgres

# Docker's Service names
APP_SERVICE_NAME := api
POSTGRES_SERVICE_NAME := db

# Edit these! Update with your own values
ENV_FILE_LOCATION := .env.dev
POSTGRES_USER := base


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
		
		
.PHONY: bash
bash:
		@docker exec -it $(APP_CONTAINER) bash


.PHONY: dbshell
dbshell:
		@docker exec -it $(POSTGRES_CONTAINER) psql -U $(POSTGRES_USER)


.PHONY: rebuild
rebuild:
		@$(DOCKER_COMPOSE) \
			$(DOCKER_COMPOSE_YML) \
			--env-file $(ENV_FILE_LOCATION) \
			up --detach


include make-utils/base-builds.mk