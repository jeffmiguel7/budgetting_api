LOCAL_SRC := $(CURDIR)
DOCKER_COMPOSE := docker-compose
DOCKER_COMPOSE_YML := --file docker-compose.yml
SUCCESS_MESSAGE := "✅ My base app is running on http://localhost:3000"
ENV_FILE_LOCATION := .env.dev
APP_CONTAINER := runserver
POSTGRES_CONTAINER := postgres
POSTGRES_USER := postgres


.PHONY: up
up:
		@$(DOCKER_COMPOSE) \
			$(DOCKER_COMPOSE_YML) \
			--env-file $(ENV_FILE_LOCATION) \
			$@ --build --detach
		@echo $(SUCCESS_MESSAGE)
		
		
.PHONY: bash
bash:
		@docker exec -it $(APP_CONTAINER) bash


.PHONY: dbshell
dbshell:
		@docker exec -it $(POSTGRES_CONTAINER) psql -U $(POSTGRES_USER)


include make-utils/base-builds.mk