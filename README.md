[![Build Status](https://travis-ci.org/nearjay06/api_iReporter.svg?branch=develop)](https://travis-ci.org/nearjay06/api_iReporter)

[![Coverage Status](https://coveralls.io/repos/github/nearjay06/api_iReporter/badge.svg?branch=develop)](https://coveralls.io/github/nearjay06/api_iReporter?branch=develop)

[![Maintainability](https://api.codeclimate.com/v1/badges/db3adc0af34643761152/maintainability)](https://codeclimate.com/github/nearjay06/api_iReporter/maintainability)


# IREPORTER

iReporter is a platform that enables citizens to report incidences of corruption to local authorities and also bring to attention issues that require government intervention.Users can use the platform to create red-flag records,get all red-flag records,get specific red-flag records,edit specific red-flag records and delete red-flag records.

## GETTING STARTED

- On your computer or laptop, download and install the VS source code editor
- Create a folder on your computer or laptop and give it the "iReporter project" name
- Open the folder in VS code editor
- In a web browser such as Google chrome,create a git hub repository
- Use the Vs source code editor, to initializing your git hub repo i.e $git init

## PREREQUSITES

- Use a pivotal tracker board to manage the project
- Download and install python3 and postman on your laptop or computer. Postman is an HTTP client
  for testing web services.
- In VS code,install the flask micro web framework i.e $pip install flask
- Also in VS code,pip install coveralls and requirements.txt 
- Integrate the project with Travis CI
- Get coveralls and code climate badges
- Host it on Heroku

## RUNNING THE PROJECT

- Run the project code in the VS code editor by typing,"python run.py"

## ENDPOINTS

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `api/v1/red-flags` | `POST`  | Creates a new red-flag|
| `api/v1/red-flags` | `GET`  | Gets red-flag records|
| `api/v1/red-flags/<int:incident-id>` | `GET` | Retrieves a specific red-flag| 
| `api/v1/red-flags/<int:incident-id>/location` | `PATCH` | Update a redflag location|
| `api/v1/red-flags/<int:incident-id>/comment` | `PATCH` | Update a red-flag comment |
| `api/v1/red-flags/<int:incident-id>` | `DELETE`  | Delete a red-flag|
| `api/v1/interventions` | `POST`  | Creates a new intervention|
| `api/v1/interventions` | `GET`  | Gets interventions records|
| `api/v1/interventions/<int:incident-id>` | `GET`  | Gets a specific intervention|
 | `api/v1/interventions/<int:incident-id>/location` | `PATCH`  | Updates intervention location |
| `api/v1/interventions/<int:incident-id>/comment` | `PATCH`  | Upadtes intervention comment|
| `api/v1/interventions` | `DELETE`  | Deletes and intervention record|
| `api/v1/users` | `POST`  | Creates a new user|
| `api/v1/users` | `GET`  | Gets all users|
| `api/v1/users/<int:user-id>` | `GET`  | Gets specific user record|
| `api/v1/users` | `DELETE`  | Deletes a user record|


## BUILT WITH

- python3
- flask

## AUTHOR

Okecho Joan

## ACKNOWLEDGEMENTS

Andela-Uganda

