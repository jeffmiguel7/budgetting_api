# Budgetting Web App: API service

## Requirements

#### If you're developing on Windows:

- Run Powershell as administrator
- Install chocolatey
- Install Docker Desktop
- Install docker-cli, if not already installed _(choco install docker-cli)_
- Install docker-compose, if not already installed _(choco install docker-compose)_
- Install make _(choco install make)_

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
    POSTGRES_USER=
    POSTGRES_PASS=
   ```

3. Enter the base directory and run `make up`.

### Make

#### core commands

`make up` builds the image, builds and runs the containers, and detaches from those containers. <br/>
`make stop` stops the specified Docker services running. <br/>
`make runserver` runs the specified Docker services. <br/>
`make bash` accesses the terminal in the specified container via an _interactive tty_. <br/>
`make dbshell` accesses the Postgres' terminal `psql` in the specified container with the Postgres database using the `-U` option w/ the correct Postgres user. <br/>
`make rebuild` rebuilds the connected services, if necessary. <br/>

#### extended commands

`make base-docker-build` explicitly builds the image with the docker command. <br/>
`make base-docker-run` explicitly runs a named single app container using the specified image, port forwards from port 8000 of the container to port 3000 of the host machine, and runs an _interactive tty_ terminal in the newly created container.
