include .env
export
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)
DOCKER_COMPOSE = docker compose
PG_URI = postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}:5432
DB_NAME = ${POSTGRES_DB}

TARGET_MAX_CHAR_NUM=15

.DEFAULT_GOAL := help

## Show this help message
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			sub(/:/, "", helpCommand); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
.PHONY: help


## Bring up docker environment
up:
	$(DOCKER_COMPOSE) up -d
.PHONY: up

## Bring up docker environment (no daemon mode)
run:
	$(DOCKER_COMPOSE) up
.PHONY: up


## Bring down docker environment
down:
	$(DOCKER_COMPOSE) down
.PHONY: down


## Connect to API container shell
backend:
	$(DOCKER_COMPOSE) exec backend bash
.PHONY: backend


# Bring up postgres, API AND frontend
frontend:
	cd frontend && yarn start
.PHONY: frontend

## Generate an empty SQLAlchemy revision script. The script needs to be edited manually with the upgrade and downgrade changes
revision:
	@read -p "Enter revision message: " MESSAGE; echo "Generating revision with message: $${MESSAGE}"; \
	$(DOCKER_COMPOSE) exec backend bash -c "poetry run alembic revision --autogenerate -m \"$${MESSAGE}}\""
.PHONY: revision


## Run SQLAlchemy migrations to bring db up to date
upgrade:
	$(DOCKER_COMPOSE) exec backend bash -c "poetry run alembic upgrade"
.PHONY: upgrade


## Run pytest in backend container
# test:
# 	clear && $(DOCKER_COMPOSE) exec backend bash -c "source venv/bin/activate && pytest"
# .PHONY: test


## Lint backend and frontend
# lint:
# 	clear && $(DOCKER_COMPOSE) exec backend bash -c "./etc/lint.sh"
# 	$(DOCKER_COMPOSE) exec frontend bash -c "./scripts/lint.sh"
# .PHONY: lint-and-test


## Drops the current development DB and generates it completely from scratch
# recreate-local-db:
# 	$(DOCKER_COMPOSE) stop backend
# 	$(DOCKER_COMPOSE) exec postgresql bash -c "echo 'drop database if exists $(DB_NAME)' | psql $(PG_URI) && echo 'create database $(DB_NAME)' | psql $(PG_URI)"
# 	$(DOCKER_COMPOSE) start backend
# 	$(DOCKER_COMPOSE) exec backend bash -c "source venv/bin/activate && flask db upgrade"
