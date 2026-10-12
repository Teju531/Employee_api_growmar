# Day 1 – Employee API Project

## Work Completed

Today, I started developing an Employee API using Python and FastAPI. I created the initial project structure and organized the application code, test files, documentation, and sample employee data into separate folders.

I implemented a health-check endpoint (`GET /health`) to verify that the API is running correctly. I also configured environment variables using Pydantic Settings and created `.env` and `.env.example` files to manage application configuration.

Next, I created a Dockerfile and a Docker Compose configuration to run the FastAPI application and PostgreSQL database together. I successfully started the containers and verified that the API returned a successful response.

I wrote a test for the health-check endpoint and ran it using Pytest. The test passed successfully. I also prepared an API contract documenting the planned employee endpoints and created a JSON file containing 10 sample employee records.

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic Settings
- PostgreSQL
- Docker and Docker Compose
- Pytest

## Current Status

The initial project setup is complete, and the health-check endpoint is working correctly. Docker configuration, environment settings, testing, API documentation, and sample employee data have been prepared.

## Next Steps

- Implement employee CRUD endpoints.
- Connect the API to PostgreSQL.
- Add validation for employee data.
- Test the employee endpoints.
- Verify that environment secrets are excluded from Git commits.