from flask import Flask, jsonify, request
from flask_jwt import JWT
from api.models.incident import Incidents, Redflags, redflags_list
from api.controllers import control
import json
from api.validations import valid
from api import app
from api.secure.safe import token_required

 
@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'


@app.route('/api/v1/redflags',methods=['POST'])
# @token_required
def report_redflag():
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

    
    redflag = Redflags(incident_id,created_on,created_by,incident_type,location,
                         status,images,videos,comment)
    if control.save(redflag) !=True:
        return control.save(redflag)
    return jsonify({
         'status': 201,
         'data': redflag.to_dict_redflag(),
         'message': 'Created red flag record'
    }),200

  
@app.route('/api/v1/redflags',methods=['GET'])
# @token_required
def get_all_redflag_records():
    return jsonify({'status': 200,
                    'data': redflags_list}),200
    
@app.route('/api/v1/redflags/<int:incident_id>',methods=['GET'])
# @token_required
def get_specific_redflag_record_with_id(incident_id):
    return control.get_specific_redflag(incident_id)
    
@app.route('/api/v1/redflags/<int:incident_id>/location',methods=['PATCH'])
# @token_required
def edit_redflag_record_location_with_id(incident_id):
    return control.edit_location(incident_id)
    
@app.route('/api/v1/redflags/<int:incident_id>/comment',methods=['PATCH'])
# @token_required
def edit_redflag_record_comment_with_id(incident_id):
    return control.edit_comment(incident_id)
  
@app.route('/api/v1/redflags/<int:incident_id>', methods=['DELETE'])
# @token_required
def delete_specific_redflag_record_with_id(incident_id):
    return control.delete_redflag(incident_id)
  
  

