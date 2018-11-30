from flask import jsonify,request
from api.models.user import user_list
from api.validations import user_valid
from api.validations.user_valid import certify_phone_number_with_user_id


def check_phone_number_user_id(user_id):
  use = request.get_json()
  phone_number = use.get('phone_number')
  if not certify_phone_number_with_user_id(phone_number):
    return jsonify({'message':'invalid phone_number'}),400
  for user in user_list:
    if user['user_id'] == user_id:
      user['phone_number'] = phone_number
      return jsonify({'message':'phone number has been updated'}),200

  return jsonify({'message':'phone number has not been updated'}),400

def check_email_user_id(user_id):
  use = request.get_json()
  email = use.get('email')
  for user in user_list:
    if user['user_id'] == user_id:
      user['email'] = email
      return jsonify({'message':'email has been updated'}),200
  return jsonify({'message':'email has not been updated'}),400
  

def delete_user(user_id):
  for user in user_list:
    print(user)
    if user['user_id'] == user_id:
      user_list.remove(user)

      return jsonify({'message':'user has been removed'}),200
  return jsonify ({'message':'user is has not been removed'}),410 
 

    