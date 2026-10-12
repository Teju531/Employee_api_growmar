# Employee API Contract

## Overview

The Employee API is designed to manage employee information. It will allow users to view employee details, add new employees, update existing records, and delete employees when needed.

## Base URL

`http://localhost:8080`

## 1. Check API Status

**GET `/health`**

This endpoint checks whether the API is running properly. It is useful for testing the application and confirming that the server is available.

**Example response:**
```json
{
  "status": "ok"
}
```

## 2. View All Employees

**GET `/employees`**

This endpoint will return a list of all employees stored in the system.

**Example response:**
```json
[
  {
    "id": 1,
    "name": "Arun Kumar",
    "email": "arun@example.com",
    "department": "Engineering",
    "job_title": "Software Developer"
  }
]
```

## 3. View an Employee

**GET `/employees/{employee_id}`**

This endpoint will return the details of a specific employee using their employee ID.

- `200 OK` — Employee details are returned successfully.
- `404 Not Found` — No employee exists with the given ID.

## 4. Add a New Employee

**POST `/employees`**

This endpoint will be used to add a new employee to the system. The request should include the employee's name, email, department, and job title.

**Example request:**
```json
{
  "name": "Priya Sharma",
  "email": "priya@example.com",
  "department": "HR",
  "job_title": "HR Executive"
}
```

- `201 Created` — Employee added successfully.
- `422 Unprocessable Entity` — The submitted data is invalid.

## 5. Update Employee Details

**PUT `/employees/{employee_id}`**

This endpoint will allow users to update an employee's existing information. The employee ID identifies which record needs to be updated.

- `200 OK` — Employee details updated successfully.
- `404 Not Found` — Employee does not exist.
- `422 Unprocessable Entity` — The submitted data is invalid.

## 6. Delete an Employee

**DELETE `/employees/{employee_id}`**

This endpoint will remove an employee's record from the system using their employee ID.

- `204 No Content` — Employee deleted successfully.
- `404 Not Found` — Employee does not exist.

## Employee Information

Each employee record will contain the following fields:

- **id:** A unique number assigned to each employee.
- **name:** The employee's full name.
- **email:** The employee's email address.
- **department:** The department in which the employee works.
- **job_title:** The employee's role in the company.

## Current Progress

The API health-check endpoint has been implemented and tested successfully. The remaining employee endpoints are documented here as the next features to be developed.