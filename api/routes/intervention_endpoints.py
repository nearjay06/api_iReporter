from flask import Flask, jsonify, request
from api.models.incident import Incidents,Interventions
from api.validations.valid import validate_status, check_created_by,check_location,check_comment
from api.validations.valid import check_videos,validate_redflags_list, validate_images
from api.validations.valid import validate_incident_id

import json

app = Flask(__name__)

interventions_list = []

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

    interventions = Incidents(incident_id,created_on,created_by,location,
                              status,images,videos,comment)
    interventions_list.append(interventions.to_dict_intervention())
    return jsonify(interventions_list),201

@app.route('/api/v1/interventions',methods=['GET'])
def get_all_intervention_records():
    return jsonify({'interventions_list': interventions_list}),201

@app.route('/api/v1/interventions/<int:incident_id>',methods=['GET'])
def get_specific_intervention_record_with_id(incident_id):
  for intervention in interventions_list:
    validate_incident_id(incident_id)
   
  return jsonify({'interventions_list':interventions_list,
                   'message':'intervention is in the list'}),200

@app.route('/api/v1/interventions/<int:incident_id>/location',methods=['PATCH'])
def update_intervention_record_location_with_id(incident_id):
  
  location = ["300.64 N", "81.63 E"]
  float_list = [ float(x) for x in location]
  print (float_list) 

  data = data.get_json()
  location = data.get('location')
  for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['location'] = location
      return jsonify({'interventions_list':interventions_list,
                      'message': 'location has been updated'}),200
    return jsonify({'message':'location has not been updated'}),400

    interventions_list.append(interventions_list)


@app.route('/api/v1/interventions/<int:incident_id>/comment',methods=['PATCH'])
def update_intervention_comment_with_id(incident_id):
  data = request.get_json()
  comment = data.get('comment')
  for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['comment'] = comment
      return jsonify({'interventions_list': interventions_list,
                      'message':'comment has been updated'}),200
    return jsonify({'message':'comment has not been updated'}),400


@app.route('/api/v1/interventions/<int:incident_id>', methods=['DELETE'])
def delete_specific_intervention_with_id(incident_id):
  for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      interventions_list.remove(intervention)

      return jsonify({'message':'intervention has been deleted'}),200
    return jsonify ({'message':'old intervention record is still in the list'}),410