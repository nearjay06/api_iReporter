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

   for red-flag in incidents:
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
