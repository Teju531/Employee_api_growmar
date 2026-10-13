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

# Employee API — Day 2

## 1. Database Models
- Created Employee, Department, Role, and EmployeeRole tables.
- Added relationships between employees, departments, and roles.
- Added fields like email, manager ID, timestamps, and active status.

## 2. ER Diagram

The ER diagram shows how the tables are connected.

**ER Diagram Image:**

![alt text](<Untitled diagram_2026-10-13T12_42_57.044Z.jpeg>)

![Employee API ER Diagram](docs/er_diagram.png)

## 3. Database Migrations
- Configured Alembic to manage database changes.
- Applied the migration successfully to create the tables.
- Tested upgrade and rollback successfully using a separate test database.

## 4. Manager Hierarchy
- An employee can have another employee as their manager.
- The manager relationship works in both directions.
- An employee cannot be their own manager.

## 5. Constraint Tests
- Tested that duplicate employee emails are rejected.
- Tested that an employee can have a manager.
- Tested that an employee cannot be their own manager.

## 6. Day 2 Summary
- Created the database models and relationships.
- Applied and tested database migrations.
- Verified the manager hierarchy and database constraints.