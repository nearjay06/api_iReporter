from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)

incidents_list = []
users_list = []

@app.route('/api/v1/redflags/<int:redflagid>/location',methods=['PATCH'])
def edit_redflag_record_location_with_id(incidentid):
  for redflags in incidents_list:
    if redflags['incidentid'] == incidentid:
      redflags.patch('location')
      return jsonify({'message': 'location has been updated'}),200
    return jsonify({'message':'location has not been updated'}),400

incidents_list.append(incidents_list)

@app.route('/api/v1/<int:redflag>/comment',methods=['PATCH'])
def edit_redflag_record_comment_with_id(incidentid):
  for redflags in incidents_list:
    if redflags['incidentid'] == incidentid:
      redflags.patch('comment')
      return jsonify({'message':'comment has been updated'}),200
    return jsonify({'message':'comment has not been updated'}),400

