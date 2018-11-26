from flask import Flask, jsonify, request
from api.models.incident import Incidents
import json
from api.validations.valid import validate_status, check_created_by,check_location,check_comment
from api.validations.valid import check_videos,validate_redflags_list, validate_images
app = Flask(__name__)

redflags_list = []

@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'

@app.route('/api/v1/redflags',methods=['POST'])
def post_redflag_records():
    request = request.get_json()

    incident_id = len(redflags_list)+1
    created_on = request.get('createdOn')
    created_by = request.get('createdBy')
    incident_type = request.get('incident_type')
    location = request.get('location')
    status = request.get('status')
    images = request.get('images')
    videos = request.get('videos')
    comment = request.get('comment')

    for redflags in redflags_list:
      check_created_by(created_by)

      validate_redflags_list(redflags_list)
     
      check_location(location)
    
      validate_status(status)
     
      validate_images(images)
    
      check_videos(videos)
    
      check_comment(comment)


    redflags = Incidents(incident_id,created_on,created_by,incident_type,location,
                         status,images,videos,comment)
    redflags_list.append(redflags.create_redflag())
    return jsonify(redflags_list),201


@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
    if redflags_list == redflags_list:
      return jsonify({'reflags_list': redflags_list}),200
    return jsonify({'message':'there are no redflags in the list'}),400
  

@app.route('/api/v1/redflags/<int:incident_id>',methods=['GET'])
def get_specific_redflag_record_with_id(incident_id):
  for redflags in redflags_list:
   if redflags['incident_id'] == incident_id:
    return jsonify({'redflags_list':redflags_list,
                   'message':'the redflag was obtained'}),200
   return jsonify({'message':'incident id does not exist'}),400

  if not incident_id or incident_id.isspace():
   return jsonify ({'message':'invalid!redflag id is not in the system'}),400

  if not isinstance(incident_id,int):
   return jsonify({'message':'redflag id should be an integer'}),400

@app.route('/api/v1/redflags/<int:incident_id>/location',methods=['PATCH'])
def edit_redflag_record_location_with_id(incident_id):
  request = request.get_json()
  location = request.get('location')
  for redflags in redflags_list:
    if redflags['incident_id'] == incident_id:
      redflags['location'] = location
      return jsonify({'message': 'location has been updated'}),200
    return jsonify({'message':'location has not been updated'}),400

    redflags_list.append(redflags_list)

@app.route('/api/v1/<int:incident_id>/comment',methods=['PATCH'])
def edit_redflag_record_comment_with_id(incident_id):
  for redflags in redflags_list:
    if redflags['incident_id'] == incident_id:
      redflags.patch('comment')
      return jsonify({'message':'comment has been updated'}),200
    return jsonify({'message':'comment has not been updated'}),400


#PATCH/redflags/<int:redflagid>






@app.route('/api/v1/redflags', methods=['DELETE'])
def delete_redflag_records():
  for redflags in redflags_list:
    if redflags == redflags_list:
      redflags.delete(redflags_list)
      return jsonify({'message':'redflags have been deleted'}),200
  return jsonify ({'message':'redflags are still in the system'}),410
      

@app.route('/api/v1/redflags/<int:incident_id>', methods=['DELETE'])
def delete_specific_redflag_record_with_id(incident_id):
  for redflags in redflags_list:
    if redflags['incident_id'] == incident_id:
      redflags_list.delete(redflags)
      return jsonify({'message':'redflag has been deleted'}),200
    return jsonify ({'message':'redflag is still in the incidents list'}),410
      










