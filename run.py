from flask import Flask
from api.routes import redflag_endpoints,intervention_endpoints,user_endpoints
from api import app

from flask_jwt import JWT
from api.secure.safe import *
app.config['SECRET_KEY'] = 'mysecret'
jwt=JWT(app,authenticate,identity)











if __name__ == '__main__':
    app.run(debug=True)