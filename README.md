User Management REST API

A simple Flask-based REST API for managing user data with CRUD operations.

Prerequisites

Python 3.x
Flask (pip install flask)

Setup

Save the API code as app.py
Install dependencies: pip install flask
Run the application: python app.py

Endpoints

GET /users: Retrieve all users
GET /users/: Retrieve a specific user by ID
POST /users: Create a new user (requires JSON with name and email)
PUT /users/: Update an existing user (requires JSON with name and email)
DELETE /users/: Delete a user by ID

Testing

Use Postman or curl to test the API. Example curl commands:
# Create a user
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@example.com"}' http://localhost:5000/users
# Get all users
curl http://localhost:5000/users
# Get a user
curl http://localhost:5000/users/1
# Update a user
curl -X PUT -H "Content-Type: application/json" -d '{"name":"John Smith","email":"john.smith@example.com"}' http://localhost:5000/users/1
# Delete a user
curl -X DELETE http://localhost:5000/users/1

Notes

Data is stored in-memory and will be lost on server restart.
The API runs on http://localhost:5000 by default.
