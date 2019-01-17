from flask import jsonify
import re

def validate_first_name(first_name):
    if not first_name or not isinstance(first_name,str) or first_name.isspace():
        return jsonify ({'message':'first name is required and should be a string'}),400
    return True

def validate_last_name(last_name):
    if not last_name or not isinstance(last_name,str) or last_name.isspace():
        return jsonify({'message':'last name is required and should be a string'}),400
    return True

def validate_email(email):
    if not email or not isinstance (email,str) or email.isspace() or not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
        return jsonify({'message':'please provide an email'}),400
    return True

def validate_password(password):
    if not password  or not isinstance(password,str) or len(password) > 10 or password.isspace():
        return jsonify ({'message':'invalid! please provide password'}),403
    return True

def validate_username(username):
    if not username  or not isinstance(username,str) or username.isspace():
        return jsonify({'message':'sorry!please provide username and it should be a string'}),400
    return True

def validate_other_names(other_names):
    if not other_names or not isinstance(other_names,str) or other_names.isspace() :
        return jsonify({'message':'sorry!please provide correct othernames'}),400
    return True

def validate_phone_number(phone_number):
    if not phone_number or not isinstance(phone_number,str) or phone_number.isspace():
        return jsonify({'message':'please provide a valid phone number'}),400
    return True

def validate_isAdmin(isAdmin):
    if not isinstance(isAdmin,bool):
        return jsonify({'message':'admin is supposed to be a boolean'}),400
    return True

def check_user_id(user_id):
    if not user_id  or not isinstance(user_id,int) or user_id.isspace():
        return jsonify({'message':'user id is required and it should be an integer'}),400
    return True

def certify_phone_number_with_user_id(phone_number):
    return isinstance(phone_number, list)

