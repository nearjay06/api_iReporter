from flask import jsonify,request
from api.models.user import user_list
from api.validations import user_valid
from api.validations.user_valid import certify_phone_number_with_user_id


def check_phone_number_user_id(user_id):
  use = request.get_json()
  phone_number = use.get('phone_number')
  for user in user_list:
    if user['user_id'] == user_id:
      user['phone_number'] = phone_number
      return jsonify({
                      'status':200,
                      'data': user,
                      'message': 'updated phone number'}),200

  return jsonify({'message':'phone number has not been updated'}),400

def check_email_user_id(user_id):
  use = request.get_json()
  email = use.get('email')
  for user in user_list:
    if user['user_id'] == user_id:
      user['email'] = email
      return jsonify({
                      'status':200,
                      'data': user,
                      'message':'updated email address'}),200
  return jsonify({'message':'email has not been updated'}),400
  

def delete_user(user_id):
  user = [user for user in user_list if user['user_id'] == user_id ]
  user_list.remove(user[0])
  return jsonify({
                   'status': 200,
                   'data':user,
                   'message':'user has been deleted'}),200

 
def get_specific_user(user_id):
  for user in user_list:
    if user['user_id'] == user_id:
             return jsonify({'status': 200,
                             'data':user})
  return jsonify({'status':200,
                  'message':'user not found'})
    