IMAGE_NAME := budget_web_app_api
CONTAINER_NAME := budget_runserver

.PHONY: base-docker-build
base-docker-build:
		@docker image build -t $(IMAGE_NAME) .


.PHONY: base-docker-run
base-docker-run:
		@docker run -p 3000:8000 -it --name $(CONTAINER_NAME) $(IMAGE_NAME)
