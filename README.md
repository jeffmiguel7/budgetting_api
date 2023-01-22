# Budgetting Web App: API service

## Requirements

#### If you're developing on Windows:

- Run Powershell as administrator
- Install chocolatey
- Install Docker Desktop
- Install docker-cli, if not already installed → `choco install docker-cli`
- Install docker-compose, if not already installed → `choco install docker-compose`
- Install make _(choco install make)_
- Install git

#### If you're developing on MacOS:

- Install Docker Desktop
- Install docker-cli, if not already installed
- Install docker-compose, if not already installed

## Environment

### Setup

1. Clone this repo anywhere in your machine.
2. Create `.env` file in your base directory and add your initial postgres values

   ```bash
    POSTGRES_DB=
    POSTGRES_USER=postgres # default superuser
    POSTGRES_PASS=
   ```

3. Enter the base directory and run `make up`.
4. Run `make stop` to stop all services.
5. If you need to clear everything, run `make teardown` to remove the service's containers, volumes, and images.
   **_Note:_** Run `make help` to get of list of `make` targets.
