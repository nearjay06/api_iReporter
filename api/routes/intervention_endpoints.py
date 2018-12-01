from flask import Flask, jsonify, request
from api.models.incident import Incidents,Interventions
from api.controllers.control import edit_intervention_location,edit_intervention_comment
from api.controllers.control import delete_intervention,get_specific_intervention
from api.validations.valid import validate_status, check_created_by,check_location,check_comment
from api.validations.valid import check_videos,validate_images
from api.validations.valid import validate_intervention_incident_id
from api.models.incident import interventions_list
from api import app

import json

@app.route('/api/v1/interventions',methods=['POST'])
def post_intervention():
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

    
    check_created_by(created_by)

    check_location(location)
    
    validate_status(status)
     
    validate_images(images)
    
    check_videos(videos)
    
    check_comment(comment)

    interventions = Incidents(incident_id,created_on,created_by,incident_type,location,
                              status,images,videos,comment)
    interventions_list.append(interventions.to_dict_intervention())
    return jsonify({
                    'status': 200,
                    'data': interventions_list,
                    'message': 'Created intervention record'
               }),200


@app.route('/api/v1/interventions',methods=['GET'])
def get_all_intervention_records():
  return jsonify({'status': 200,
                  'data': interventions_list}),200
   
@app.route('/api/v1/interventions/<int:incident_id>',methods=['GET'])
def get_specific_intervention_record_with_id(incident_id):
  return get_specific_intervention(incident_id)

  validate_intervention_incident_id(incident_id)
  

@app.route('/api/v1/interventions/<int:incident_id>/location',methods=['PATCH'])
def update_intervention_record_location_with_id(incident_id):
  return edit_intervention_location(incident_id)
  

@app.route('/api/v1/interventions/<int:incident_id>/comment',methods=['PATCH'])
def update_intervention_comment_with_id(incident_id):
  return edit_intervention_comment(incident_id)
  
@app.route('/api/v1/interventions/<int:incident_id>', methods=['DELETE'])
def delete_specific_intervention_with_id(incident_id):
  return delete_intervention(incident_id)
  