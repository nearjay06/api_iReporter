from flask import Flask, jsonify, request 
from flask_jwt import JWT
from api.models.user import Users, user_list,Admin,admin_access
from api.controllers import user_control
import json
from api import app
from api.secure.safe import *


@app.route('/api/v1/users/signup',methods=['POST'])
def user_signup():
    use = request.get_json()

    user_id = len(user_list)+1
    first_name = use.get('first_name')
    last_name =  use.get('last_name')
    other_names = use.get('other_names')
    email = use.get('email')
    phone_number = use.get('phone_number')
    username = use.get('username')
    password = use.get('password')
    registered = use.get('registered')
    
    
    user = Users(user_id, first_name, last_name, other_names, email, phone_number,
                  username,password, registered)
    # user_list.append(user)
    if user_control.client(user)!=True:
      return user_control.client(user)
    return jsonify({
                      'status': 201,
                      'data': user.user_dict(),
                      'message': 'Created user'
                }),201


@app.route('/api/v1/admins/signup',methods=['POST'])
def admin_signup():
    use = request.get_json()

    user_id = len(user_list)+1
    first_name = use.get('first_name')
    last_name =  use.get('last_name')
    other_names = use.get('other_names')
    email = use.get('email')
    phone_number = use.get('phone_number')
    username = use.get('username')
    password = use.get('password')
    registered = use.get('registered')
    
      
    admin = Admin(user_id, first_name, last_name, other_names, email, phone_number,
                  username,password, registered)
    # user_list.append(admin)
    if user_control.client(admin)!=True:
      return user_control.client(admin)
    return jsonify({
                      'status': 201,
                      'data': admin.user_dict(),
                      'message': 'Created admin account'
                }),201


@app.route('/api/v1/users/signin',methods=['POST'])
def user_signin():
    details = request.get_json()
    username = details.get('username')
    password = details.get('password')
    
    if user_control.login(username,password)!=True:
        return user_control.login(username,password)
    generated_token = encode_token(username)
    return jsonify({
                      'status': 201,
                      'message':'User has signed in',
                      'token': generated_token.decode('utf-8')
                }),201

@app.route('/api/v1/users',methods=['GET'])
# @token_required
def get_all_users():
    return jsonify({'status': 200,
                    'data': user_list}),200
    
# @app.route('/api/v1/users',methods=['GET'])
# @token_required
# def get_all_users():
    # return user_control.get_all_users()
    #  user = admin_access()
    # if user:
    #      view_users = []
    #      for user in user_list:
    #          view_users.append(user.user_dict())

    #     return jsonify({'status': 200,
    #                 'data': view_users}),200
    #  else:
    #      return jsonify ({'message':'Access is only for the Admin'})
    





@app.route('/api/v1/users/<int:user_id>',methods=['GET'])
# @token_required
def get_specific_user_with_id(user_id):
    return user_control.get_specific_user(user_id)


@app.route('/api/v1/users/<int:user_id>/phone_number',methods=['PATCH'])
# @token_required
def edit_phone_number_with_user_id(user_id):
    return user_control.check_phone_number_user_id(user_id)

  
@app.route('/api/v1/users/<int:user_id>/email',methods=['PATCH'])
# @token_required
def edit_user_email_with_id(user_id):
    return user_control.check_email_user_id(user_id)
    

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
# @token_required
def delete_specific_user_with_id(user_id):
    return user_control.delete_user(user_id)
    

