from flask import Flask, jsonify, request
from flask_jwt import JWT
from api.models.incident import Incidents,Interventions,interventions_list
from api.controllers import control
from api.validations import valid
from api import app
import json
from api.secure.safe import token_required


@app.route('/api/v1/interventions',methods=['POST'])
# @token_required
def create_intervention():
  
    data = request.get_json()

    incident_id = len(interventions_list)+1
    created_on = data.get('created_on')
    created_by = data.get('created_by')
    incident_type = data.get('incident_type')
    location = data.get('location')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    comment = data.get('comment')

        
    intervention = Interventions(incident_id,created_on,created_by,incident_type,location,
                              status,images,videos,comment)
    # interventions_list.append(intervention) 
    if control.save(intervention)!=True:
      return control.save(intervention)
    return jsonify({
                      'status': 200,
                      'data': intervention.to_dict_intervention(),
                      'message': 'Created intervention record'
                }),200


@app.route('/api/v1/interventions',methods=['GET'])
# @token_required
def get_all_intervention_records():
  return jsonify({'status': 200,
                  'data': interventions_list}),200
   

@app.route('/api/v1/interventions/<int:incident_id>',methods=['GET'])
# @token_required
def get_specific_intervention_record_with_id(incident_id):
  return control.get_specific_intervention(incident_id)


@app.route('/api/v1/interventions/<int:incident_id>/location',methods=['PATCH'])
# @token_required
def update_intervention_record_location_with_id(incident_id):
  return control.edit_intervention_location(incident_id)
  
@app.route('/api/v1/interventions/<int:incident_id>/comment',methods=['PATCH'])
# @token_required
def update_intervention_comment_with_id(incident_id):
  return control.edit_intervention_comment(incident_id)

@app.route('/api/v1/interventions/<int:incident_id>', methods=['DELETE'])
# @token_required
def delete_specific_intervention_with_id(incident_id):
  return control.delete_intervention(incident_id)
  