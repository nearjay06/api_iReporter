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

    validate_other_names(other_names)

    validate_phone_number(phone_number)


    users = Users(user_id, first_name, last_name, other_names, email, phone_number,
                  username, registered,isAdmin)
    user_list.append(users.user_dict())
    return jsonify(user_list),201

@app.route('/api/v1/users',methods=['GET'])
def get_all_users():
    return jsonify({'user_list': user_list}),200


@app.route('/api/v1/users/<int:user_id>',methods=['GET'])
def get_specific_user_with_id(user_id):
    for user in user_list:
     check_user_id(user_id)

    return jsonify({'user_list':user_list,
                    'message':'user is in the list'}),200
  
@app.route('/api/v1/users/<int:user_id>/phone_number',methods=['PATCH'])
def edit_phone_number_with_user_id(user_id):
    use = request.get_json()
    phone_number = use.get('phone_number')
    for user in user_list:
        if user['user_id'] == user_id:
            user['phone_number'] = phone_number
            return jsonify({'message':'phone number has been updated'}),200

        return jsonify({'message':'phone number has not been updated'}),400
    
    user_list.append(user_list)


@app.route('/api/v1/users/<int:user_id>/email',methods=['PATCH'])
def edit_user_email_with_id(user_id):
    use = request.get_json()
    email = use.get('email')
    for user in user_list:
        if user['user_id'] == user_id:
            user['email'] = email
            return jsonify({'message':'email has been updated'}),200

        return jsonify({'message':'email has not been updated'}),400
    
    user_list.append(user_list)


@app.route('/api/v1/users/<int:incident_id>', methods=['DELETE'])
def delete_specific_user_with_id(user_id):
    for user in user_list:
        if user['user_id'] == user_id:
            user_list.remove(user)

        return jsonify({'message':'user has been deleted'}),200
    return jsonify ({'message':'user is still in the list'}),410