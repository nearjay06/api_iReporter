from flask import jsonify
import re



def validate_inputs(first_name,last_name,email,password,username,other_names,phone_number,
                     isAdmin):

    if not first_name:   
        return  ['first name is required',400]
    
    if not isinstance(first_name,str):
        return ['first name must be a string',400]
    
    if first_name.isspace():
        return ['first name cannot be blank',400]
    
    if not last_name:
        return  ['last name is required',400]

    if not isinstance(last_name,str):
        return ['last name must not be a number',400]
    
    if  last_name.isspace():
            return ['last name is required',400]
         
     
    if not isinstance(email,str):
            return [' email must not be a number',400]

    if not email or  email.isspace() or not isinstance(email,str):
            return ['please provide a valid email',400]

    if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
        return ['invalid!  an important symbol may be missing in the email provided',400]

    if not isinstance(password,str):
        return ['password must not be a number',400]    
        
    if  len(password) > 10:
            return ['invalid! password should be less or equal to 10 characters',400] 
         
    if not password or password.isspace():
            return ['invalid! please provide correct password',400]

    if not isinstance(username,str):
        return ['username must not be a number',400]

    if not username or username.isspace():
        return ['sorry!please provide  username',400]

    if not isinstance(other_names,str):
        return ['othernames must not be a number',400]           
    
    if not other_names or other_names.isspace() :
            return ['sorry!please provide correct othernames',400]

    if  not isinstance(phone_number,str):
            return ['phone number should be a string',400]

    if not phone_number or phone_number.isspace():
            return ['please provide a valid phone number',400]

    if not isinstance(phone_number,str):
        return ['phone number must not be a letter',400] 

    # if not isinstance(isAdmin,bool):
    #     return ['admin is supposed to be a boolean',400]
    
def validate_needed(username,password):
    if not isinstance(username,str):
        return ['username must not be a number',400]    

    if not username or username.isspace():
        return ['sorry!please provide  username',400]

    if not isinstance(password,str):
        return ['password must not be a number',400]  

    if  len(password) > 10:
            return ['invalid! password should be less or equal to 10 characters',400]      
    
    if not password or password.isspace():
            return ['invalid! password is required',400]
    
    



def check_user_id(user_id):
    if not user_id  or not isinstance(user_id,int) or user_id.isspace():
        return jsonify({'message':'user id is required and it should be an integer'}),400
    return True

def certify_phone_number_with_user_id(phone_number):
    return isinstance(phone_number, list)

