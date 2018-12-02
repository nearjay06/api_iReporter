from flask import jsonify


def validate_first_name(first_name):
    if not first_name or not isinstance(first_name,str) or first_name.isspace():
        return jsonify ({'message':'first_name is required'}),401

def validate_last_name(last_name):
    if not last_name or not isinstance(last_name,str) or last_name.isspace():
        return jsonify({'message':'last name is required'}),400

def validate_email(email):
    if not email or not isinstance (email,int) or email.isspace():
        return jsonify({'message':'please provide an email'}),401

def validate_username(username):
    if not username or username.isspace() or isinstance(username,int):
        return jsonify({'message':'sorry!please provide username and it should be a string'}),400

def validate_other_names(other_names):
    if not other_names or other_names.isspace() or isinstance(other_names,int):
        return jsonify({'message':'sorry!please provide othernames'}),400

def validate_phone_number(phone_number):
    if not phone_number or phone_number.isspace() or not isinstance(phone_number,str):
        return jsonify({'message':'please provide phone number'}),400

def validate_registered(registered):
    if not registered or registered.isspace() or not isinstance(registered,str):
        return jsonify({'message':'date is required'}),400

def check_user_id(user_id):
    if not user_id  or isinstance(user_id,str) or user_id.isspace():
        return jsonify({'message':'user id is required and it should be an integer'}),400

def certify_phone_number_with_user_id(phone_number):
    return isinstance(phone_number, list)

