from flask import Flask, jsonify, request
from api.models.user import Users
from api.controllers.user_control import check_phone_number_user_id,get_specific_user
from api.controllers.user_control import check_email_user_id,delete_user

import json
from api.validations.user_valid import validate_first_name,validate_last_name,validate_email
from api.validations.user_valid import validate_username,validate_other_names,validate_phone_number
from api.validations.user_valid import check_user_id,validate_registered 
from api.models.user import user_list
from api import app


@app.route('/api/v1/users',methods=['POST'])
def post_user_record():
    use = request.get_json()

    user_id = len(user_list)+1
    first_name = use.get('first_name')
    last_name =  use.get('last_name')
    other_names = use.get('other_names')
    email = use.get('email')
    phone_number = use.get('phone_number')
    username = use.get('username')
    registered = use.get('registered')
    isAdmin = use.get('isAdmin')

    validate_first_name(first_name)

    validate_last_name(last_name)

    validate_email(email)

    validate_username(username)

    validate_registered(registered)

    validate_other_names(other_names)

    validate_phone_number(phone_number)

    users = Users(user_id, first_name, last_name, other_names, email, phone_number,
                  username, registered,isAdmin)
    user_list.append(users.user_dict())
    return jsonify({
                    'status': 201,
                    'data': user_list,
                    'message': 'Created user record'
                                }),200


@app.route('/api/v1/users',methods=['GET'])
def get_all_users():
    return jsonify({'status': 200,
                    'data': user_list}),200
    
@app.route('/api/v1/users/<int:user_id>',methods=['GET'])
def get_specific_user_with_id(user_id):
    return get_specific_user(user_id)

    check_user_id(user_id)

@app.route('/api/v1/users/<int:user_id>/phone_number',methods=['PATCH'])
def edit_phone_number_with_user_id(user_id):
    return check_phone_number_user_id(user_id)
     
@app.route('/api/v1/users/<int:user_id>/email',methods=['PATCH'])
def edit_user_email_with_id(user_id):
    return check_email_user_id(user_id)
    
  
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_specific_user_with_id(user_id):
    return delete_user(user_id)
    