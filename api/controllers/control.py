
from flask import jsonify,request
from api.models.incident import Interventions, Redflags,Incidents
from api.validations.valid import validate_redflag_location_with_id 
from api.validations.valid import validate_intervention_location_with_id
from api.models.incident import redflags_list,interventions_list
from api.validations.valid import validate_images,validate_incident_id,validate_incident_type
from api.validations.valid import validate_status,check_comment,check_videos,check_created_by
from api.validations.valid import check_location


def save(resource):
  if  check_created_by(resource.created_by) != True:
    return check_created_by(resource.created_by)

  if check_location(resource.location) !=True:
    return check_location(resource.location)
    
  if validate_status(resource.status)!=True:
    return validate_status(resource.status)

  if validate_images(resource.images)!=True:
    return validate_images(resource.images)
    
  if check_videos(resource.videos)!=True:
    return check_videos(resource.videos)
    
  if check_comment(resource.comment) !=True:
    return check_comment(resource.comment)

  if validate_incident_type(resource.incident_type)!=True:
    return validate_incident_type(resource.incident_type)

  if isinstance(resource, Interventions):
    Incidents.interventions_list.append(resource.to_dict_intervention())
    print(Incidents.interventions_list)
    return True
  else:
    print(Incidents.redflags_list)
    Incidents.redflags_list.append(resource.to_dict_redflag())
    return True

def edit_location(incident_id):
  request_data = request.get_json()
  location = request_data.get('location')
  for redflag in Incidents.redflags_list:
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
 for redflag in Incidents.redflags_list:
    if redflag['incident_id'] == incident_id:
      redflag['comment'] = comment
      return jsonify({
                      'status':200,
                      'data': redflag,
                      'message':'updated red-flag record comment'}),200
 return jsonify({'message':'red-flag record comment has not been updated'}),400


def delete_redflag(incident_id): 
  redflag = [redflag for redflag in Incidents.redflags_list if redflag['incident_id'] == incident_id ]
  if len(redflag) == 0:
    return jsonify({'message':'redflag does not exist'}),400
  Incidents.redflags_list.remove(redflag[0])
  return jsonify({'status': 200,
                  'data':redflag,
                  'message':'redflag record has been deleted'})
  
  
def edit_intervention_location(incident_id):
 data = request.get_json()
 location = data.get('location')
 for intervention in Incidents.interventions_list:
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
 for intervention in Incidents.interventions_list:
    if intervention['incident_id'] == incident_id:
      intervention['comment'] = comment
      return jsonify({
                    'status':200,
                    'data':intervention,
                    'message':'updated intervention record comment'}),200
 return jsonify({'message':'intervention record comment has not been updated'}),400

def delete_intervention(incident_id):
  intervention = [intervention for intervention in Incidents.interventions_list if intervention['incident_id'] == incident_id ]
  if len(intervention) == 0:
    return jsonify({'message':'intervention does not exist'}),400
  
  Incidents.interventions_list.remove(intervention[0])
  return jsonify({
                   'status': 200,
                   'data':intervention,
                   'message':'interventon record has been deleted'}),200

def get_specific_redflag(incident_id):
  for redflag in Incidents.redflags_list:
    if redflag['incident_id'] == incident_id:
             return jsonify({'status': 200,
                             'data':redflag})
  return jsonify({'status':200,
                  'message':'redflag record not found'})

def get_specific_intervention(incident_id):
  for intervention in Incidents.interventions_list:
    if intervention['incident_id'] == incident_id:
             return jsonify({'status': 200,
                             'data':intervention})
  return jsonify({'status':200,
                  'message':'intervention record not found'})