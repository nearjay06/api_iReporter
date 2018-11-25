from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)


incidents = []
users = []

#to delete a redflag record DELETE/redflags
@app.route('api/v1/redflags', methods=['DELETE'])
def delete_redflag_records():
  for redflags in incidents:
    if redflags == incidents:
      del redflags
      return jsonify({'message':'redflags have been deleted'}),200
    return jsonify ({'message':'redflags are still in the system'}),410
      
#to delete a  specific redflag record DELETE/redflags/<int:redflagid>
@app.route('api/v1/redflags/<int:redflagid>', methods=['DELETE'])
def delete_redflag_record_with_id(incidentid):
  for redflags in incidents:
    if redflags['incidentid'] == incidentid:
      del incidents[redflags]
      return jsonify({'message':'redflag has been deleted'}),200
    return jsonify ({'message':'redflag is still in the incidents list'}),410