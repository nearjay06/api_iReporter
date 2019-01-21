from flask import Flask, jsonify, request 
from flask_jwt import JWT
from api.models.user import Users, user_list,Admin,admin_access
from api.controllers import user_control
import json
from api import app
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
    
    user = Users( first_name, last_name, other_names, email, phone_number,
                  username,password)    
    user_id = db.insert_users(user.first_name ,user.last_name , user.other_names, user.email,
              user.phone_number,user.username,
                    user.password, user.registered,user.isAdmin)
                  
    return jsonify({
                      'status': 201,
                       'user_id': user_id,
                      'message': 'Created user data in user database'
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
    
      
    admin = Users( first_name, last_name, other_names, email, phone_number,
                  username,password)    
    db.insert_users(admin.first_name ,admin.last_name , admin.other_names, admin.email,admin.phone_number,
                    admin.username,admin.password, admin.registered,admin.isAdmin)
    return jsonify({
                      'status': 201,
                       'user_id': user_id,
                       'message': 'Created admin data in user database'
                }),201


@app.route('/api/v2/auth/signin',methods=['POST'])
def user_signin():
    details = request.get_json()
    email = details.get('email')
    password = details.get('password')
    
    user = db.get_specific_user()
    if email == user[4] and password == user[7]:
        generated_token = encode_token(username)
        return jsonify({
                        'status': 200,
                        'message':'User has signed in',
                        'token': generated_token.decode('utf-8')
                    }),200
    return "wrong username or password"

@app.route('/api/v2/users',methods=['GET'])
@token_required
def get_all_users(present_user):
    user ="""SELECT * FROM user_data"""
    if user:
        return jsonify({'status': 200,
                    'data': user}),200
    
@app.route('/api/v2/users/<int:user_id>',methods=['GET'])
@token_required
def get_specific_user_with_id(present_user,user_id):
    return user_control.get_specific_user(user_id)




