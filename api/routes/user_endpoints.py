from flask import Flask, jsonify, request 
from flask_jwt import JWT
from api.models.user import Users, user_list,Admin,admin_access
from api.controllers import user_control
import json
from api import app
from api.validations.user_valid import validate_inputs,validate_needed
from api.secure.safe import *

from api.database.db import DatabaseConnection

db = DatabaseConnection()


@app.route('/api/v2/auth/signup',methods=['POST'])
def user_signup():
    use = request.get_json()
    
          
    first_name = use.get('first_name')
    last_name =  use.get('last_name')
    other_names = use.get('other_names')
    email = use.get('email')
    phone_number = use.get('phone_number')
    username = use.get('username')
    password = use.get('password')
    isAdmin = use.get('isAdmin')
    
        
    
    invalid = validate_inputs(first_name,last_name,email,password,username,other_names,phone_number,
                              isAdmin)
    if invalid:
        return jsonify({'message':str(invalid[0])}),invalid[1]

    user = Users( first_name, last_name, other_names, email, phone_number,
                  username,password)  
    db_user= db.insert_users(user.first_name ,user.last_name , user.other_names, user.email,
              user.phone_number, user.username, user.password, user.registered,  user.isAdmin)
    generated_token = encode_token(username)           
    return jsonify({
                      'status': 201,
                      'token':generated_token.decode('utf-8'),
                      'user': db_user
                  }),201


@app.route('/api/v2/auth/admins/signup',methods=['POST'])
def admin_signup():
    use = request.get_json()

    first_name = use.get('first_name')
    last_name =  use.get('last_name')
    other_names = use.get('other_names')
    email = use.get('email')
    phone_number = use.get('phone_number')
    username = use.get('username')
    password = use.get('password')
    isAdmin = use.get('isAdmin')
    
    
    invalid = validate_inputs(first_name,last_name,email,password,username,other_names,phone_number,
                     isAdmin)
    if invalid:
        return jsonify({'message':str(invalid[0])}),invalid[1]   
    admin = Users( first_name, last_name, other_names, email, phone_number,username,password)    
    db_admin = db.insert_admins(admin.first_name ,admin.last_name , admin.other_names, admin.email,
                  admin.phone_number,admin.username,admin.password, admin.registered,admin.isAdmin)
    generated_token = encode_token(username)
    return jsonify({
                      'status': 201,
                      'token':generated_token.decode('utf-8'),
                      'user': db_admin                      
                }),201


@app.route('/api/v2/auth/signin',methods=['POST'])
def user_signin():
    details = request.get_json()
    username = details.get('username')
    password = details.get('password')
    
        
    incorrect = validate_needed(username,password)
    if incorrect:
        return jsonify({'message':str(incorrect[0])}),incorrect[1] 
    user = db.get_specific_user(username,password)

    if user != None:
        generated_token = encode_token(username)
        return jsonify({
                            'status': 200,
                            'u':user,
                            'token': generated_token.decode('utf-8')
                        }),200
    else:
        return jsonify({'message':'user is non existent'})

@app.route('/api/v2/auth/users',methods=['GET'])
@token_required
def get_all_users(present_user):
    user = get_users()
    if user:
        generated_token = encode_token(username)
        return jsonify({'status': 200,
                    'data': user,
                    'token': generated_token.decode('utf-8')
                    
                }),200
    