from flask import Flask, jsonify, request
from api.models.user import Users
import json
from api.validations.user_valid import validate_first_name,validate_last_name,validate_email
from api.validations.user_valid import validate_username,validate_other_names,validate_phone_number
from api.validations.user_valid import check_user_id 
# update_phone_number

app = Flask(__name__)

user_list = []

@app.route('/api/v1/users',methods=['POST'])
def post_user_record():
   data = request.get_json()

   user_id = len(user_list)+1
   first_name = data.get('first_name')
   last_name =  data.get('last_name')
   other_names = data.get('other_names')
   email = data.get('email')
   phone_number = data.get('phone_number')
   username = data.get('username')
   registered = data.get('registered')
   isAdmin = data.get('isAdmin')


   for user in user_list:
    validate_first_name(first_name)

    validate_last_name(last_name)

    validate_email(email)

    validate_username(username)

    validate_other_names(other_names)

    validate_phone_number(phone_number)


    users = Users(user_id, first_name, last_name, other_names, email, phone_number,
                  username, registered,isAdmin)
    user_list.append(users.user_dictionary())
    return jsonify(user_list),201

@app.route('/api/v1/users',methods=['GET'])
def get_all_users():
    return jsonify({'user_list': user_list}),200


@app.route('/api/v1/users/<int:user_id>',methods=['GET'])
def get_specific_user_with_id(user_id):
    for user in user_list:
     check_user_id(user_id)

    return jsonify({'user_list':user_list}),201
  
# @app.route('/api/v1/users/<int:user_id>/phonenumber',methods=['PATCH'])
# def edit_phone_number_with_user_id(user_id,phone_number):
#     for user in user_list:
#      update_phone_number(phone_number)

#     return jsonify({'message': 'phonenumber has been updated'}),200
#     user_list.append(user_list)

# def edit_redflag_record_location_with_id(incident_id):
#  @app.route('/api/v1/<int:user_id>/comment',methods=['PATCH'])
# def edit_redflag_record_comment_with_id(incident_id):
#  @app.route('/api/v1/users', methods=['DELETE'])
# def delete_user():
#  @app.route('/api/v1/redflags/<int:incident_id>', methods=['DELETE'])
# def delete_specific_user_with_id(user_id):