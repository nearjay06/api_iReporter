from flask import Flask, jsonify, request
from api.models.incident import Incidents
from api.models.user import Users
app = Flask(__name__)


incidents = []
users = []

@app.route('/api/v1/redflags/<int:redflagsid>',methods=['GET'])
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
