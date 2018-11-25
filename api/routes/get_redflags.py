from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)


incidents = []
users = []

@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
   for redflags in incidents():
    if incidents == incidents:
     return jsonify({'incidents': incidents}),200
    return jsonify({'message':'there are no redflags in the incidents list'}),400