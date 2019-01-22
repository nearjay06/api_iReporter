from flask import jsonify,request
from api.models.user import Users,user_list,Admin,admin_access
from api.validations.user_valid import *
from api.validations.user_valid import certify_phone_number_with_user_id

# from api.validations.user_valid import validate_username,validate_other_names,validate_phone_number
# from api.validations.user_valid import check_user_id,validate_password,validate_isAdmin



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
  if len(user) == 0:
    return jsonify({'message':'user is not in the list'}),400
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


def get_all_users():
  user = admin_access()
  if user:
    view_users = []
    for user in user_list:
      view_users.append(user.user_dict())
      return jsonify({'status': 200,
                    'data': view_users}),200
  else:
    return jsonify ({'message':'Access is only for the Admin'})
