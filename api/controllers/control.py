
from flask import jsonify,request
from api.validations.valid import validate_redflag_location_with_id 
from api.validations.valid import validate_intervention_location_with_id
from api.models.incident import redflags_list,interventions_list


def edit_location(incident_id):
  request_data = request.get_json()
  location = request_data.get('location')
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['location'] = location
      return jsonify({
                      'status':200,
                      'data': redflag,
                      'message': 'updated red-flag record location'}),200
  return jsonify({'message':'red-flag record location has not been updated'}),400


def edit_comment(incident_id):
 request_data = request.get_json()
 comment = request_data.get('comment')
 for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['comment'] = comment
      return jsonify({
                      'status':200,
                      'data': redflag,
                      'message':'updated red-flag record comment'}),200
 return jsonify({'message':'red-flag record comment has not been updated'}),400


def delete_redflag(incident_id): 
  redflag = [redflag for redflag in redflags_list if redflag['incident_id'] == incident_id ]
  redflags_list.remove(redflag[0])
  return jsonify({'status': 200,
                  'data':redflag,
                  'message':'redflag record has been deleted'})
  
  #return jsonify({'message':'redflag is still in the list'}),400

def edit_intervention_location(incident_id):
 data = request.get_json()
 location = data.get('location')
 for intervention in interventions_list:
   if intervention['incident_id'] == incident_id:
     intervention['location'] = location
     return jsonify({
                    'status':200,
                    'data': intervention,       
                    'message':'updated intervention record location'}),200
 return jsonify({'message':'intervention record location has not been updated'}),400

def edit_intervention_comment(incident_id):
 data = request.get_json()
 comment = data.get('comment')
 for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['comment'] = comment
      return jsonify({
                    'status':200,
                    'data':intervention,
                    'message':'updated intervention record comment'}),200
 return jsonify({'message':'intervention record comment has not been updated'}),400

def delete_intervention(incident_id):
  intervention = [intervention for intervention in interventions_list if intervention['incident_id'] == incident_id ]
  interventions_list.remove(intervention[0])
  return jsonify({
                   'status': 200,
                   'data':intervention,
                   'message':'interventon record has been deleted'}),200

#return jsonify ({'message':'intervention record is still in the list'}),410 

def get_specific_redflag(incident_id):
  for redflag in redflags_list:
    if redflag['incident_id'] == incident_id:
             return jsonify({'status': 200,
                             'data':redflag})
  return jsonify({'status':200,
                  'message':'redflag record not found'})

def get_specific_intervention(incident_id):
  for intervention in interventions_list:
    if intervention['incident_id'] == incident_id:
             return jsonify({'status': 200,
                             'data':intervention})
  return jsonify({'status':200,
                  'message':'intervention record not found'})