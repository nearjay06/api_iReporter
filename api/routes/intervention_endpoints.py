from flask import Flask, jsonify, request
from flask_jwt import JWT
from api.models.incident import Incidents,Interventions,interventions_list
from api.controllers import control
from api.validations.valid import validate_interventions
from api import app
import json
from api.secure.safe import token_required
from api.database.db import DatabaseConnection

db = DatabaseConnection()


@app.route('/api/v2/interventions',methods=['POST'])
@token_required
def create_intervention(username):
  
    data = request.get_json()
  
    created_by = data.get('created_by')
    incident_type = data.get('incident_type')
    location = data.get('location')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    comment = data.get('comment')

    wrong_intervention = validate_interventions(created_by,incident_type,location,
                                                status, images, videos, comment)
    if wrong_intervention:
        return jsonify({'message':str(wrong_intervention[0])}),wrong_intervention[1] 

    intervention = Incidents(created_by,incident_type,location,status,images,videos,comment)
    db_intervention = db.put_incidents(intervention.created_on,intervention.created_by,
                            intervention.incident_type,intervention.location,
                            intervention.status,intervention.images,intervention.videos,
                            intervention.comment)
    
    return jsonify({
                      'status': 200,
                      'intervention': db_intervention,
                      'message': 'Created intervention record'
                      
                }),200


@app.route('/api/v1/interventions',methods=['GET'])
# @token_required
def get_all_intervention_records(present_user):
  return jsonify({'status': 200,
                  'data': interventions_list}),200
   

@app.route('/api/v1/interventions/<int:incident_id>',methods=['GET'])
# @token_required
def get_specific_intervention_record_with_id(present_user,incident_id):
  return control.get_specific_intervention(incident_id)


@app.route('/api/v1/interventions/<int:incident_id>/location',methods=['PATCH'])
# @token_required
def update_intervention_record_location_with_id(present_user,incident_id):
  return control.edit_intervention_location(incident_id)
  
@app.route('/api/v1/interventions/<int:incident_id>/comment',methods=['PATCH'])
# @token_required
def update_intervention_comment_with_id(preset_user,incident_id):
  return control.edit_intervention_comment(incident_id)

@app.route('/api/v1/interventions/<int:incident_id>', methods=['DELETE'])
# @token_required
def delete_specific_intervention_with_id(present_user,incident_id):
  return control.delete_intervention(incident_id)
  