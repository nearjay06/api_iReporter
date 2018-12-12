from flask import jsonify,request
from api.models.user import Users,user_list
from api.validations import user_valid
from api.validations.user_valid import certify_phone_number_with_user_id
from api.validations.user_valid import validate_first_name,validate_last_name,validate_email
from api.validations.user_valid import validate_username,validate_other_names,validate_phone_number
from api.validations.user_valid import check_user_id,validate_password,validate_isAdmin


def client(reserve):
  if validate_first_name(reserve.first_name)!=True:
    return validate_first_name(reserve.first_name)

  if validate_last_name(reserve.last_name)!= True:
     return validate_last_name(reserve.last_name)

  if validate_email(reserve.email)!= True:
    return validate_email(reserve.email)

  if validate_username(reserve.username)!=True:
    return validate_username(reserve.username)

  if validate_password(reserve.password)!= True:
    return validate_password(reserve.password)

  if validate_other_names(reserve.other_names)!=True:
    return validate_other_names(reserve.other_names)

  if validate_phone_number(reserve.phone_number)!=True:
    return validate_phone_number(reserve.phone_number)
  
  if validate_isAdmin(reserve.isAdmin)!= True:
    return validate_isAdmin(reserve.isAdmin)
     
  if isinstance(reserve, Users):
    Users.user_list.append(reserve.user_dict())
    print(Users.user_list)
    return True


def login(username,password):
  
  if validate_username(username)!=True:
    return validate_username(username)

  if validate_password(password)!= True:
    return validate_password(password)

  return True
 

def check_phone_number_user_id(user_id):
  use = request.get_json()
  phone_number = use.get('phone_number')
  for user in Users.user_list:
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
  for user in Users.user_list:
    if user['user_id'] == user_id:
      user['email'] = email
      return jsonify({
                      'status':200,
                      'data': user,
                      'message':'updated email address'}),200
  return jsonify({'message':'email has not been updated'}),400
  

def delete_user(user_id):
  user = [user for user in Users.user_list if user['user_id'] == user_id ]
  if len(user) == 0:
    return jsonify({'message':'user is not in the list'}),400
  Users.user_list.remove(user[0])
  return jsonify({
                   'status': 200,
                   'data':user,
                   'message':'user has been deleted'}),200

 
def get_specific_user(user_id):
  for user in Users.user_list:
    if user['user_id'] == user_id:
             return jsonify({'status': 200,
                             'data':user})
  return jsonify({'status':200,
                  'message':'user not found'})

    