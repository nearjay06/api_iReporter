from flask import Flask, jsonify, request
from flask_jwt import JWT
from api.models.incident import Incidents, Redflags, redflags_list
from api.controllers import control
import json
from api.validations import valid
from api import app
from api.secure.safe import token_required
from api.validations.valid import validate_redflags
from api.database.db import DatabaseConnection

db = DatabaseConnection()

 
@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'


@app.route('/api/v2/redflags',methods=['POST'])
@token_required
def report_redflag(present_user):
    request_data = request.get_json()

    created_by = request_data.get('created_by')
    incident_type = request_data.get('incident_type')
    location = request_data.get('location')
    status = request_data.get('status')
    images = request_data.get('images')
    videos = request_data.get('videos')
    comment = request_data.get('comment')

    wrong_redflag = validate_redflags(created_by,incident_type,location,
                                                status, images, videos, comment)
    if wrong_redflag:
        return jsonify({'message':str(wrong_redflag[0])}),wrong_redflag[1] 

    redflag = Incidents(created_by,incident_type,location,status,images,videos,comment)
    db_redflag = db.put_incidents(redflag.created_on,redflag.created_by,
                            redflag.incident_type,redflag.location,
                            redflag.status,redflag.images,redflag.videos,
                            redflag.comment)
    
    return jsonify({
                      'status': 200,
                      'data': db_redflag,
                      'message': 'Created redflag record'
                      
                }),200

    
     
@app.route('/api/v2/redflags',methods=['GET'])
@token_required
def get_all_redflag_records(present_user):
    redflags = db.get_incidents('redflag')
    return jsonify({'status': 200,
                  'data': redflags}),200

    
@app.route('/api/v2/redflags/<int:incident_id>',methods=['GET'])
@token_required
def get_specific_redflag_record_with_id(present_user,incident_id):
        special_redflag = db.redflag_id(incident_id, 'redflag')
        if db.redflag_id(incident_id, 'redflag'):
          return jsonify({
                    'status':200,
                      'data': special_redflag,
                      'incident_id': incident_id

                    }),200

        else:
          return jsonify({'message':'redflag is not in the list'}),400

@app.route('/api/v2/redflags/<int:incident_id>/status',methods=['PATCH'])
@token_required
def edit_redflag_status(present_user,incident_id):

  redflag_status_changed= db.redflag_status(incident_id,'status')
  
  return jsonify({
                 'status':200,
                 'incident_id': incident_id,
                'message':'updated redflag status'

                }),200


@app.route('/api/v2/redflags/<int:incident_id>/location',methods=['PATCH'])
@token_required
def edit_redflag_location(present_user,incident_id):

  redflag_location= db.redflag_location(incident_id, 'location')
  return jsonify({
                 'status':200,
                 'incident_id': incident_id,
                 'message':'updated redflag location'

                }),200


@app.route('/api/v2/redflags/<int:incident_id>/comment',methods=['PATCH'])
@token_required
def update_redflag(preset_user,incident_id):

  updated_comment= db.redflag_incident_comment(incident_id, 'comment')
  return jsonify({
                 'status':200,
                  'incident_id': incident_id,
                  'message':'update redflag comment'

                }),200

    
@app.route('/api/v2/redflags/<int:incident_id>', methods=['DELETE'])
@token_required
def delete_redflag(present_user,incident_id):

  deleted = db.remove_redflag(incident_id, 'redflag')
  return jsonify({
                 'status':200,
                  'incident_id': incident_id,
                  'message':'deleted redflag'

                }),200





    

  

  

