from flask import Flask, jsonify, request
from api.models.incident import Incidents,Redflags
import json
from api.validations.valid import validate_status, check_created_by,check_location,check_comment
from api.validations.valid import check_videos,validate_images
from api.validations.valid import validate_incident_id

app = Flask(__name__)

redflags_list = []

@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'

@app.route('/api/v1/redflags',methods=['POST'])
def post_redflag_records():
    request = request.get_json()

    incident_id = len(redflags_list)+1
    created_on = request.get('created_on')
    created_by = request.get('created_by')
    incident_type = request.get('incident_type')
    location = request.get('location')
    status = request.get('status')
    images = request.get('images')
    videos = request.get('videos')
    comment = request.get('comment')

    check_created_by(created_by)

    check_location(location)
    
    validate_status(status)
     
    validate_images(images)
    
    check_videos(videos)
    
    check_comment(comment)


    redflags = Incidents(incident_id,created_on,created_by,location,status,images,videos,comment)
    redflags_list.append(redflags.to_dict_redflag())
    return jsonify(redflags_list),201


@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
  return jsonify({'reflags_list': redflags_list}),200
    

@app.route('/api/v1/redflags/<int:incident_id>',methods=['GET'])
def get_specific_redflag_record_with_id(incident_id):
  for redflag in redflags_list:
    validate_incident_id(incident_id)
   
  return jsonify({'redflags_list':redflags_list,
                   'message':'redflag is in the list'}),200
   
  
@app.route('/api/v1/redflags/<int:incident_id>/location',methods=['PATCH'])
def edit_redflag_record_location_with_id(incident_id):
  
  location = ["100.34 N", "50.57 E"]
  float_list = [ float(x) for x in location]
  print (float_list) 
  
  location = request.get('location')
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['location'] = location
      return jsonify({'message': 'location has been updated'}),200
    return jsonify({'message':'location has not been updated'}),400

    redflags_list.append(redflags_list)

@app.route('/api/v1/redflags/<int:incident_id>/comment',methods=['PATCH'])
def edit_redflag_record_comment_with_id(incident_id):
  request = request.get_json()
  comment = request.get('comment')
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['comment'] = comment
      return jsonify({'message':'comment has been updated'}),200
    return jsonify({'message':'comment has not been updated'}),400


@app.route('/api/v1/redflags/<int:incident_id>', methods=['DELETE'])
def delete_specific_redflag_record_with_id(incident_id):
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflags_list.remove(redflag)

      return jsonify({'message':'redflag has been deleted'}),200
    return jsonify ({'message':'redflag is still in the list'}),410
      










