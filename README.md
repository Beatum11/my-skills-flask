# My Skills API

## Overview
My Skills API is a Flask-based web service that allows users to view, add, update, or delete skills on a single endpoint `/skills`. Utilizing pymongo for interaction with a MongoDB database, this API serves as a dynamic resume of sorts, showcasing the variety and level of skills.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete skills.
- **MongoDB Integration**: Utilizes pymongo for database interaction.
- **Single Endpoint**: All operations are performed on the `/skills` endpoint.

## Prerequisites
- Python 3.7+
- pip
- MongoDB connection string

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/my-skills-api.git
    cd my-skills-api
    ```

2. Install the required dependencies:
    ```bash
    pip install python-dotenv
    pip install pymongo
    pip install flask
    ```

3. Setup MongoDB:
    - Ensure that you have MongoDB connection string

4. Run the Flask application:
    ```bash
    flask run
    ```

## Usage
- **Read Skills**
    - Method: GET
    - Endpoint: `/skills`
    - Description: Retrieve a list of all skills.
  
- **Add Skill**
    - Method: POST
    - Endpoint: `/skills`
    - Description: Add a new skill.
    - Body: 
        ```json
        {
            "name": "Python",
            "content": "Python is a..."
        }
        ```

- **Update Skill**
    - Method: PUT
    - Endpoint: `/skills/<skill_id>`
    - Description: Update an existing skill.
    - Body:
        ```json
        {
            "name": "C#"
        }
        ```
  
- **Delete Skill**
    - Method: DELETE
    - Endpoint: `/skills/<skill_id>`
    - Description: Delete an existing skill.
