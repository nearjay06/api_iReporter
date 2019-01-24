from flask import Flask
from api.routes import redflag_endpoints,intervention_endpoints,user_endpoints
from api import app
from api.database.db import DatabaseConnection

db = DatabaseConnection()

from flask_jwt import JWT
from api.secure.safe import *
app.config['SECRET_KEY'] = 'mysecret'
# jwt=JWT(app,authenticate,identity)

if __name__ == '__main__':
    db.create_table_incidents()
    db.create_table_users()
    app.run(debug=True)