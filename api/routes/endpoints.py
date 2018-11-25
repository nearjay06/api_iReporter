from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)


incidents = []
users = []

#post redflag records POST/red-flags
@app.route ('/api/v1/red-flags',methods=['POST'])
def post_red_flag_records():
   flags = request.get_json()

   incidentid = len(incidents)+1
   createdOn = flags.get('createdOn')
   createdBy = flags.get('createdBy')
   type   = flags.get('type')
   location = flags.get('location')
   status = flags.get('status')
   images = flags.get('images')
   videos = flags.get('videos')
   comment = flags.get('comment')

   for redflag in incidents:
    if isinstance(incidentid,str):
      return jsonify ({'message':'incident id must not be a string'}),400
    return jsonify({'incidents': incidents}),201

    if not createdBy or createdBy.isspace():
     return jsonify ({'message':'invalid! creator name is required'}),400

    if incidents == []:
     return jsonify ({'message':'there are no incidents in the list'}),400

    if not location:
     return jsonify({'message':'sorry!location of the incident is required'}),400
    return jsonify({'incidents':incidents}),201

    if status == " ":
     return jsonify ({'message':'incident status is missing'}),400
    return jsonify ({'incidents':incidents}),200

    if not images or len(images) == 0:
     return jsonify ({'message':'sorry! the red-flagshould have an image'}),400
    return jsonify ({'incidents':incidents}),201

    if not videos or len(videos) == 0:
     return jsonify({'message':'a video is required for the red-flag'}),400
    return jsonify ({'incidents': incidents})
    
    if not comment:
     return jsonify({'message':'comments are needed for the redflag'}),400


    incident = Incidents(incidentid,createdOn,createdBy,type,location,status,images,videos,comment)
    incidents.append(incidents)
    return jsonify(incidents),201


#to get all red-flag records GET/red-flags
@app.route('/api/v1/redflags',methods=['GET'])
def get_all_redflag_records():
   for redflags in incidents():
    if incidents == incidents:
     return jsonify({'incidents': incidents}),200
    return jsonify({'message':'there are no redflags in the incidents list'}),400

#to get a specific red-flag record with an id GET/red-flags/<int:red-flag id>
@app.route('/api/v1/redflags/<int:redflag id',methods=['GET'])
def get_specific_redflag_record_with_id(incidentid):
  for redflag in incidents:
   if redflag['incidentid'] == incidentid:
    return jsonify({'incidents':incidents,
                   'message':'the red flag was obtained'}),200
   return jsonify({'message':'incident id does not exist'}),400

  if not incidentid or incidentid.isspace():
   return jsonify ({'message':'invalid!incident id is not in the system'}),400

  if not isinstance(incidentid,int):
   return jsonify({'message':'redflag id should be an integer'}),400












