
from flask import jsonify,request
from api.validations.valid import validate_redflag_location_with_id 
from api.validations.valid import validate_intervention_location_with_id
from api.models.incident import redflags_list,interventions_list


def edit_location(incident_id):
  request_data = request.get_json()
  location = request_data.get('location')
  if not validate_redflag_location_with_id(location):
    return jsonify({'error':'invalid location data'}),400
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['location'] = location
      return jsonify({'message': 'location has been updated'}),200
  return jsonify({'message':'location has not been updated'}),400


def edit_comment(incident_id):
 request_data = request.get_json()
 comment = request_data.get('comment')
 for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['comment'] = comment
      return jsonify({'message':'comment has been updated'}),200
 return jsonify({'message':'comment has not been updated'}),400


def delete_redflag(incident_id):
 for redflag in redflags_list:
    print(redflag)
    if redflag['incident_id'] == incident_id:
      redflags_list.remove(redflag)

      return jsonify({'message':'redflag has been deleted'}),200
 return jsonify ({'message':'redflag is still in the list'}),410 

 
def edit_intervention_location(incident_id):
  data = request.get_json()
  location = request.get('location')
  if not validate_intervention_location_with_id(location):
    return jsonify({'error':'invalid location data'}),400
  for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['location'] = location
      return jsonify({'message': 'location has been updated'}),200
  return jsonify({'message':'location has not been updated'}),400


def edit_intervention_comment(incident_id):
 data = request.get_json()
 comment = data.get('comment')
 for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['comment'] = comment
      return jsonify({'message':'comment has been updated'}),200
 return jsonify({'message':'comment has not been updated'}),400

def delete_intervention(incident_id):
 for intervention in interventions_list:
    print(intervention)
    if intervention['incident_id'] == incident_id:
      interventions_list.remove(intervention)

      return jsonify({'message':'intervention has been deleted'}),200
 return jsonify ({'message':'intervention is still in the list'}),410 
