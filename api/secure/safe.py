from werkzeug.security import safe_str_cmp
from api.models.user import Users, user_list
from flask import Flask,jsonify,request
from flask_jwt import JWT,jwt_required
from functools import wraps
import jwt
import datetime
from api import app

app.config['SECRET_KEY'] = 'mysecret'


def encode_token(user_id):
    try:
        payload = {
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
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
    # token = jwt.header['payload']
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify ({'message':'token is missing'}),401
        
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'invalid token'}),401

        return f(*args, **kwargs)
    return decorated


def present_user(req):
    token = req.headers('token')
    decode_token = decode_token('token')

    if token:
        try:
            user_id = int(decode_token['user_id'])
            users = Users.user_dict.first()

            for user in users:
                if user['user_id']== user_id:
                    return user
            else:
                return False
        except jwt.ExpiredSignatureError:
            return False
    else:
        return False 


def admin_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        isAdmin = present_user()['isAdmin']
        if isAdmin:
            return f(*args, **kwargs)
        return jsonify({"message": "Access granted to admin only"}), 403
    return wrap
  
def not_admin_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        isAdmin = present_user()['isAdmin']
        if not isAdmin:
            return jsonify({"messsage": "Access for non admin only"}), 403
        return f(*args, **kwargs)
    return wrap






















































def authenticate (username,password):
    user = username.get(username,None)
    if user and safe_str_cmp(user.password,password):
     return user

def identity(payload):
    user_id = payload['identity']
    return user_id.get(user_id,None)




