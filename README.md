# RESTful API Example

**English** | [繁體中文](README.zh-TW.md)

A simple RESTful API built with Flask and SQLite for managing users. You can:

- Create a user
- Delete a user
- List all users
- Create many users at once by uploading a CSV file
- Get the average age for each group of names that start with the same letter

## Quick start

### Prerequisites

Python 3.10 or later. A virtual environment is recommended.

### Setup

1. **Create a virtual environment (recommended)**

    ```bash
    conda create -n restful_server python=3.10
    conda activate restful_server
    ```

2. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Run

1. **Run the server locally**

    ```bash
    python3 app.py
    ```

    The API is available at `http://127.0.0.1:5000`, and the API docs (Swagger UI) at `http://127.0.0.1:5000/apidocs/`.

2. **Run with Docker**

    - **Build the image:**

      ```bash
      docker build -t restful-api .
      ```

    - **Run the container:**

      ```bash
      docker run -p 5000:5000 -v $(pwd):/app restful-api
      ```

    The API is then available at `http://127.0.0.1:5000`.

## API endpoints

### 1. **Create a user**
   - **Endpoint:** `POST /user`
   - **Parameters:**
     - `name` (string, required)
     - `age` (integer, required)
   - **Responses:**
     - `200 OK` when the user is created
     - `400 Bad Request` when the input is invalid or the user already exists

### 2. **Delete a user by name**
   - **Endpoint:** `DELETE /user/<string:name>`
   - **Parameters:**
     - `name` (string, required): the user to delete
   - **Responses:**
     - `200 OK` when the user is deleted
     - `404 Not Found` when the user doesn't exist

### 3. **List all users**
   - **Endpoint:** `GET /users`
   - **Responses:**
     - `200 OK` with the list of users

### 4. **Create users from a CSV file**
   - **Endpoint:** `POST /users/upload_csv`
   - **Parameters:**
     - `file` (file, required): a CSV file with `name` and `age` columns
   - **Responses:**
     - `200 OK` when the file is uploaded and the users are created

### 5. **Average age by first letter**
   - **Endpoint:** `GET /users/average-age`
   - **Responses:**
     - `200 OK` with the average age of each group

## Project structure

```plaintext
.
├── app.py               # Flask application entry point
├── config.py            # settings
├── models/              # database model and schema
│   └── user.py
├── services/            # user operations
│   └── user_service.py
├── views/               # API routes
│   └── user_views.py
├── tests/               # unit tests
│   └── test_app.py
├── requirements.txt     # Python dependencies
└── Dockerfile           # container image
```
