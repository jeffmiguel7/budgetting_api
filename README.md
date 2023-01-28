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
   POSTGRES_DB_NAME=budgetting_api
   POSTGRES_USER=postgres
   POSTGRES_PASS=<your-password>
   PLAID_CLIENT_ID=<plaid-client-id>
   PLAID_DEVELOPMENT_SECRET=<plaid-prod-secret>
   PLAID_SANDBOX_SECRET=<plaid-sandbox-secret>

   # Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
   # password: pass_good)
   # Use `development` to test with live users and credentials and `production`
   # to go live
   PLAID_ENV=sandbox

   # PLAID_PRODUCTS is a comma-separated list of products to use when initializing
   # Link. Note that this list must contain 'assets' in order for the app to be
   # able to create and retrieve asset reports.
   PLAID_PRODUCTS=assets,transactions

   # PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
   # will be able to select institutions from.
   PLAID_COUNTRY_CODES=

   ```

3. Enter the base directory and run `make up`.
4. Run `make stop` to stop all services.
5. If you need to clear everything, run `make teardown` to remove the service's containers, volumes, and images.
   **_Note:_** Run `make help` to get of list of `make` targets.
