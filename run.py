from flask import Flask
from api.routes.redflag_endpoints import app
from api.routes.user_endpoints import app
from api.routes.intervention_endpoints import app













if __name__ == '__main__':
    app.run(debug=True)