from flask import jsonify



def validate_status(status):
    if status.isspace() or not status or not isinstance(status,str):
        return jsonify ({'message':'status is not in the list'}),400

def check_created_by(created_by):
    if not created_by or not isinstance(created_by,str) or created_by.isspace():
        return jsonify({'message':'createdby should be a string'}),400
  
def check_location(location):
    if not location or location.isspace():
        return jsonify({'message':'location is required'}),400

def check_comment(comment):
    if not comment or isinstance(comment,int) or comment.isspace():
        return jsonify({'message':'comment is required and should be a string'}),400

def check_videos(videos):
    if not videos or len(videos) == 0 or videos.isspace():
        return jsonify({'message':'a video is required for the red-flag'}),400

def validate_incident_type(incident_type):
    if not incident_type or isinstance(incident_type,int) or incident_type.isspace():
        return jsonify({'message':'incident type is required and should be a string'}),400


def validate_images(images):
    if not images or len(images) == 0 or not isinstance(images,str) or images.isspace():
        return jsonify ({'message':'sorry! the red-flag should have an image which should be a string'}),400

def validate_incident_id(incident_id):
    if not incident_id or not isinstance(incident_id,int) or incident_id <= 0 or incident_id.isspace():
        return jsonify ({'message':'invalid!redflag incident id is not in the system'}),400

def validate_intervention_incident_id(incident_id):
    if not incident_id or not isinstance(incident_id,int) or incident_id <= 0 or incident_id.isspace():
        return jsonify ({'message':'invalid!intervention incident id is not in the system'}),400

def validate_redflag_location_with_id(location):
    item1 = location[0]
    item2 = location[1]
    return isinstance(location, list) and isinstance(item1, float) and isinstance(item2, float)

def validate_intervention_location_with_id(location):
    item1 = location[0]
    item2 = location[1]
    return isinstance(location, list) and isinstance(item1, float) and isinstance(item2, float)


def validate_interventions_list(interventions_list):
    if interventions_list.isspace():
        return jsonify({'message':'there are no items in the interventions list'}),400