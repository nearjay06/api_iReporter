from flask import jsonify



def validate_interventions(created_by, incident_type, location, status, images, videos, comment):
            
    if not isinstance(status,str):
        return ['status must be a string',400]

    if not status  or status.isspace():
        return  ['status is required',400]
        
    if not created_by :
        return  ['required field is missing',400]
      
        
    if not isinstance(created_by,int):
        return ['created_by must be an integer',400]
        
    if  not isinstance(location,str):
        return ['location must be a string',400]

    if not location or location.isspace():
        return  ['location is required',400]

    if  isinstance(comment,int):
        return ['comment must be a string',400]

    if not comment or comment.isspace():
        return  ['comment is required',400]

    if not isinstance(videos,str):
        return ['video must not be a url string',400]    
        
    if  len(videos) ==0 :
            return ['invalid! please provide a video',400] 
         
    if not videos or videos.isspace():
            return ['invalid! please upload  a  video',400]

    if  not isinstance(incident_type,str):
        return ['incident type must be a string',400]

    if not incident_type or incident_type.isspace():
        return  ['incident type is required',400]  
      
    if not isinstance(images,str):
        return ['image must not be a url string',400]    
        
    if  len(images) ==0 :
            return ['invalid! please provide an image',400] 
         
    if not images or images.isspace():
            return ['invalid! please upload an image',400]
       
    
    # if not incident_id or not isinstance(incident_id,int) or incident_id <= 0 or incident_id.isspace():
    #     return jsonify ({'message':'invalid!redflag incident id is not in the system'}),400
    

def validate_intervention_incident_id(incident_id):
    if not incident_id or not isinstance(incident_id,int) or incident_id <= 0 or incident_id.isspace():
        return jsonify ({'message':'invalid!intervention incident id is not in the system'}),400
    return True

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
    return True