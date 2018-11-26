from flask import jsonify


def validate_status(status):
    if status.isspace() or not status or not isinstance(status,str):
      return jsonify ({'message':'status is not in the list'}),400

def validate_redflags_list(redflags_list):
    if redflags_list == redflags_list():
      return jsonify(redflags_list),201

def check_created_by(created_by):
    if not created_by or not isinstance(created_by,int):
      return jsonify({'message':'createdby should  be a string'}),400
  
def check_location(location):
    if not location or location.isspace:
     return jsonify({'message':'location is required'}),400

def check_comment(comment):
    if not comment or isinstance(comment,int):
     return jsonify({'message':'comment is required and should be a string'}),400

def check_videos(videos):
    if not videos or len(videos) == 0:
     return jsonify({'message':'a video is required for the red-flag'}),400

def validate_images(images):
    if not images or len(images) == 0 or not isinstance(images,str):
      return jsonify ({'message':'sorry! the red-flag should have an image which should be a string'}),400

