from flask import jsonify, request
from api.models.incident import Incidents,Redflags
from api.controllers.control import edit_location,edit_comment,delete_redflag,get_specific_redflag
import json
from api.validations.valid import validate_status, check_created_by,check_location,check_comment
from api.validations.valid import check_videos,validate_images
from api.validations.valid import validate_redflag_location_with_id
from api.validations.valid import validate_incident_id,validate_incident_type,validate_created_on
from api.models.incident import redflags_list
from api import app


@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'

@app.route('/api/v1/redflags',methods=['POST'])
def post_redflag_records():
    request_data = request.get_json()
    incident_id = len(redflags_list)+1
    created_on = request_data.get('created_on')
    created_by = request_data.get('created_by')
    incident_type = request_data.get('incident_type')
    location = request_data.get('location')
    status = request_data.get('status')
    images = request_data.get('images')
    videos = request_data.get('videos')
    comment = request_data.get('comment')

    check_created_by(created_by)

    check_location(location)
    
    validate_status(status)
     
    validate_images(images)
    
    check_videos(videos)
    
    check_comment(comment)

    validate_incident_type(incident_type)

    validate_created_on(created_on)


    redflags = Incidents(incident_id,created_on,created_by,incident_type,location,
                         status,images,videos,comment)
    redflags_list.append(redflags.to_dict_redflag())
    return jsonify({
         'status': 201,
         'data': redflags_list,
         'message': 'Created red flag record'
    }),200

@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
    return jsonify({'status': 200,
                    'data': redflags_list}),200
    

@app.route('/api/v1/redflags/<int:incident_id>',methods=['GET'])
def get_specific_redflag_record_with_id(incident_id):
    return get_specific_redflag(incident_id)
    
    validate_incident_id(incident_id)
   
@app.route('/api/v1/redflags/<int:incident_id>/location',methods=['PATCH'])
def edit_redflag_record_location_with_id(incident_id):
    return edit_location(incident_id)
    
@app.route('/api/v1/redflags/<int:incident_id>/comment',methods=['PATCH'])
def edit_redflag_record_comment_with_id(incident_id):
    return edit_comment(incident_id)
  
@app.route('/api/v1/redflags/<int:incident_id>', methods=['DELETE'])
def delete_specific_redflag_record_with_id(incident_id):
    return delete_redflag(incident_id)
  
      










