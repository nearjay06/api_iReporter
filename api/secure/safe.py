from werkzeug.security import safe_str_cmp
from api.models.user import Users, user_list
from flask import Flask,jsonify,request
from functools import wraps
import jwt
import datetime
from api import app

app.config['SECRET_KEY'] = 'mysecret'


def encode_token(user_id):
    try:
        payload = {
            'exp':datetime.datetime.utcnow() + datetime.timedelta(hours = 10),
            'iat':datetime.datetime.utcnow(),
            'sub':user_id
        }

        return jwt.encode(
            payload,
            app.config['SECRET_KEY'],
            algorithm = 'HS256'
        )

    except Exception as e:
        print(e)
        raise e

def get_token():
    if not 'Authorization' in request.headers:
        return jsonify ({'message':'token is missing'}),401
        
    token=request.headers['Authorization']
    if not token:
        return jsonify({"message":"Please login first"}),401
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token,app.config['SECRET_KEY'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired.Please sign in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token.Please sign in again.'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()

        print(token)

        if not token:
            return jsonify ({'message':'token is missing'}),401
        
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            username=data.get('username')
        except:
            return jsonify({'message':'invalid token'}),401

        return f(username,*args, **kwargs)
    return decorated
















































def authenticate (username,password):
    user = username.get(username,None)
    if user and safe_str_cmp(user.password,password):
     return user

def identity(payload):
    user_id = payload['identity']
    return user_id.get(user_id,None)




