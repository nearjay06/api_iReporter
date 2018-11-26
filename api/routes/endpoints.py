from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)

incidents_list = []
users_list = []


@app.route('/', methods=['GET'])
def reporting():
    return 'Welcome to iREPORTER'

@app.route('/api/v1/redflags',methods=['POST'])
def post_redflag_records():
   flags = request.get_json()

   incidentid = len(incidents_list)+1
   createdOn = flags.get('createdOn')
   createdBy = flags.get('createdBy')
   type   = flags.get('type')
   location = flags.get('location')
   status = flags.get('status')
   images = flags.get('images')
   videos = flags.get('videos')
   comment = flags.get('comment')

   for redflags in incidents_list:
    if isinstance(incidentid,str):
      return jsonify ({'message':'incident id must not be a string'}),400
    return jsonify({'incidents_list': incidents_list}),201

    if not createdBy or createdBy.isspace():
     return jsonify ({'message':'invalid! creator name is required'}),400

    if incidents_list == []:
     return jsonify ({'message':'there are no incidents in the list'}),400

    if not location:
     return jsonify({'message':'sorry!location of the incident is required'}),400
    return jsonify({'incidents_list':incidents_list}),201

    if status == " ":
     return jsonify ({'message':'incident status is missing'}),400
    return jsonify ({'incidents_list':incidents_list}),200

    if not images or len(images) == 0:
     return jsonify ({'message':'sorry! the red-flagshould have an image'}),400
    return jsonify ({'incidents_list':incidents_list}),201

    if not videos or len(videos) == 0:
     return jsonify({'message':'a video is required for the red-flag'}),400
    return jsonify ({'incidents_list': incidents_list})
    
    if not comment:
     return jsonify({'message':'comments are needed for the redflag'}),400


    incident = Incidents(incidentid,createdOn,createdBy,type,location,status,images,videos,comment)
    incidents_list.append(incidents_list)
    return jsonify(incidents_list),201


@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
  if incidents_list == incidents_list:
    return jsonify({'incidents_list': incidents_list}),200
  return jsonify({'message':'there are no redflags in the list'}),400
  

@app.route('/api/v1/redflags/<int:redflagid>',methods=['GET'])
def get_specific_redflag_record_with_id(incidentid):
  for redflags in incidents_list:
   if redflags['incidentid'] == incidentid:
    return jsonify({'incidents_list':incidents_list,
                   'message':'the red flag was obtained'}),200
   return jsonify({'message':'incident id does not exist'}),400

  if not incidentid or incidentid.isspace():
   return jsonify ({'message':'invalid!incident id is not in the system'}),400

  if not isinstance(incidentid,int):
   return jsonify({'message':'redflag id should be an integer'}),400

@app.route('/api/v1/redflags/<int:redflagid>/location',methods=['PATCH'])
def edit_redflag_record_location(incidentid):
  for redflags in incidents_list:
    if redflags['incidentid'] == incidentid:
      redflags.patch('location')
      return jsonify({'message': 'location has been updated'}),200
    return jsonify({'message':'location has not been updated'}),400

incidents_list.append(incidents_list)

@app.route('/api/v1/<int:redflag>/comment',methods=['PATCH'])
def edit_redflag_record_comment(incidentid):
  for redflags in incidents_list:
    if redflags['incidentid'] == incidentid:
      redflags.patch('comment')
      return jsonify({'message':'comment has been updated'}),200
    return jsonify({'message':'comment has not been updated'}),400


#PATCH/redflags/<int:redflagid>





#to delete a redflag record DELETE/redflags
@app.route('/api/v1/redflags', methods=['DELETE'])
def delete_redflag_records():
  for redflags in incidents_list:
    if redflags == incidents_list:
      redflags.delete(incidents_list)
      return jsonify({'message':'redflags have been deleted'}),200
    return jsonify ({'message':'redflags are still in the system'}),410
      
#to delete a  specific redflag record DELETE/redflags/<int:redflagid>
@app.route('/api/v1/redflags/<int:redflagid>', methods=['DELETE'])
def delete_redflag_record_with_id(incidentid):
  for redflags in incidents_list:
    if redflags['incidentid'] == incidentid:
      del incidents_list[redflags]
      return jsonify({'message':'redflag has been deleted'}),200
    return jsonify ({'message':'redflag is still in the incidents list'}),410
      










