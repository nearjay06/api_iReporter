[![Build Status](https://travis-ci.org/nearjay06/api_iReporter.svg?branch=develop)](https://travis-ci.org/nearjay06/api_iReporter)

[![Coverage Status](https://coveralls.io/repos/github/nearjay06/api_iReporter/badge.svg?branch=develop)](https://coveralls.io/github/nearjay06/api_iReporter?branch=develop)

[![Maintainability](https://api.codeclimate.com/v1/badges/db3adc0af34643761152/maintainability)](https://codeclimate.com/github/nearjay06/api_iReporter/maintainability)


## IREPORTER

iReporter is a platform that enables citizens to report incidences of corruption to local authorities and also bring to attention issues that require government intervention.Users can use the platform to create red-flag records,get all red-flag records,get specific red-flag records,edit specific red-flag records and delete red-flag records.

### GETTING STARTED

- On your computer or laptop, download and install the VS source code editor
- Create a folder on your computer or laptop and give it the "iReporter project" name
- Open the folder in VS code editor
- In a web browser such as Google chrome,create a git hub repository
- Use the Vs source code editor, to initializing your git hub repo i.e $git init
- git clone
- cd ireporter
- git checkout develop

### PREREQUSITES

- Use a pivotal tracker board to manage the project
- Download and install python3 and postman on your laptop or computer. Postman is an HTTP client
  for testing web services.
- In VS code,install the flask micro web framework i.e $pip install flask
- Also in VS code,pip install coveralls and requirements.txt 
- Integrate the project with Travis CI
- Get coveralls and code climate badges
- Host it on Heroku

### Installations

- $ pip install -r requirements.txt

### Activate Virtual Environment

- python -m virtualenv venv
- venv\Scripts\activate

### Running the Project

- Run the project code in the VS code editor by typing,"python run.py"
- Test the functionality of the endpoints using Postman

### Tests

- python -m unittest
- pytest

### ENDPOINTS

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `api/v1/red-flags` | `POST`  | Creates a new red-flag|
| `api/v1/red-flags` | `GET`  | Gets red-flag records|
| `api/v1/red-flags/<int:incident-id>` | `GET` | Retrieves a specific red-flag| 
| `api/v1/red-flags/<int:incident-id>/location` | `PATCH` | Update a redflag location|
| `api/v1/red-flags/<int:incident-id>/comment` | `PATCH` | Update a red-flag comment |
| `api/v1/red-flags/<int:incident-id>` | `DELETE`  | Delete a specific red-flag|
| `api/v1/interventions` | `POST`  | Creates a new intervention|
| `api/v1/interventions` | `GET`  | Gets interventions records|
| `api/v1/interventions/<int:incident-id>` | `GET`  | Gets a specific intervention|
| `api/v1/interventions/<int:incident-id>/location` | `PATCH`  | Updates intervention location |
| `api/v1/interventions/<int:incident-id>/comment` | `PATCH`  | Upadtes intervention comment|
| `api/v1/interventions/<int:incident-id>` | `DELETE`  | Deletes and intervention record|
| `api/v1/users/signup` | `POST`  | Creates a new user|
| `api/v1/admins/signup` | `POST`  | Creates a new admin|
| `api/v1/users/signin` | `POST`  | Users can sign in|
| `api/v1/users` | `GET`  | Gets all users|
| `api/v1/users/<int:user-id>` | `GET`  | Gets specific user record|
|`api/v1/users/<int:userid>/phonenumber` | `PATCH` | Update user phonenumber|   
|`api/v1/users/<int:userid>/email` |`PATCH`|Update user email|
| `api/v1/users/<int:userid>` | `DELETE`  | Deletes a user record|

### User Endpoint Example
 
    "data": {
        "email": "joan@gmail.com",
        "first_name": "dalai",
        "isAdmin": false,
        "last_name": "ann",
        "other_names": "mermaid",
        "password": "lalaland",
        "phone_number": "abcdefg",
        "registered": "Mon, 14 Jan 2019 17:53:13 GMT",
        "user_id": 1,
        "username": "trickster"
    },
    "message": "Created user",
    "status": 201

### Redflag Enpoint Example

    "data": {
        "comment": "like ",
        "created_by": 1234,
        "created_on": "Mon, 14 Jan 2019 17:52:40 GMT",
        "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
        "incident_id": 1,
        "incident_type": "redflag ",
        "location": "kira ",
        "status": "under investigation",
        "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc"},
    "message": "Created red flag record",
    "status": 201

### Intervention Endpoint Example

    "data": {
        "comment": "comment",
        "created_by": 1234,
        "created_on": "Mon, 14 Jan 2019 17:51:14 GMT",
        "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
        "incident_id": 1,
        "incident_type": "interventions ",
        "location": "dsdsds",
        "status": "under investigation",
        "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc" },
    "message": "Created intervention record",
    "status": 200
}

### BUILT WITH

- python3
- flask

### AUTHOR

Okecho Joan

### ACKNOWLEDGEMENTS

Andela-Uganda

