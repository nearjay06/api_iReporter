import unittest
from api.routes.user_endpoints import app
from api.models.user import Users,user_list,Admin,admin_access
from api.validations import user_valid


import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = app.test_client()
        self.user = {
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": False,
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "password":"lalaland",
            "username": "trickster"
                           
             }

    def tearDown(self):
         user_list.clear()

    def test_get_all_users(self):
        response = self.test_client.get('/api/v1/users',content_type= 'application/json')
        self.assertEqual(200,response.status_code)
        
    def test_user_signup(self):
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json',
                                         data = json.dumps(self.user))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'user id is required and it should be an integer','message'},True)
        self.assertEqual(len(self.user),9)

    def test_admin_signup(self):
        response = self.test_client.post('/api/v1/admins/signup', content_type= 'application/json',
                                  data = json.dumps(self.user))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'user id is required and it should be an integer','message'},True)
        self.assertEqual(len(self.user),9)


    def test_user_signin(self):
        items={
            "password":"lalaland",
            "username": "trickster"
                       
            }

        response = self.test_client.post('/api/v1/users/signin', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'created user','message'},True)
           
       
    def test_get_user_with_id(self):
        self.test_client.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(self.user))
        response = self.test_client.get('/api/v1/users/1')
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(self.user,dict)

    def test_update_phone_number_with_user_id(self):

        change_phone_number = {
                               "phone_number":"abcdefg"
                           }

        self.test_client.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(self.user))
        response = self.test_client.patch('/api/v1/users/1/phone_number',
                          content_type= 'application/json',data = json.dumps(change_phone_number))
        self.assertEqual(200,response.status_code)
        res = json.loads(response.data.decode())
        self.assertTrue({'updated phone number ','message'},True) 

    def test_update_user_email_with_id(self):
       
        change_email = {
                         "email": "new_email@gmail.com"
                        }

        self.test_client.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(self.user))
        response = self.test_client.patch('/api/v1/users/1/email',content_type= 'application/json', 
                                        data = json.dumps(change_email))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertTrue({"updated email address","message"},True)


    def test_delete_specific_user_with_id(self):
        self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        response = self.test_client.delete('/api/v1/users/1')
        self.assertEqual(200,response.status_code)

    def test_empty_firstname_error(self):
        self.user["first_name"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)
    
    def test_firstname_integer_error(self):
        self.user["first_name"] = 123
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_lastname_error(self):
         self.user["last_name"] = " "
         response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
         self.assertEqual(400,response.status_code)

    def test_lastname_integer_error(self):
        self.user["last_name"] = 456
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_othernames_error(self):
        self.user["other_names"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_othernames_integer_error(self):
        self.user["other_names"] = 123
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_email_error(self):
        self.user["email"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_email_integer_error(self):
        self.user["email"] = 123456
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_email_syntax_error(self):
        self.user["email"] = "joangmail"
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_password_error(self):
        self.user["password"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(403,response.status_code)

    def test_password_integer_error(self):
        self.user["password"] = 123456
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(403,response.status_code)

    def test_password_length_error(self):
        self.user["password"] = "abcdefghijklmnopqrst"
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(403,response.status_code)

    def test_username_integer_error(self):
        self.user["username"] = 1234
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_username_error(self):
        self.user["username"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_phonenumber_error(self):
        self.user["phone_number"] = " "
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)
    
    def test_phonenumber_integer_error(self):
        self.user["phone_number"] = 345678
        response = self.test_client.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_delete_specific_user_with_id_error(self):
        self.user['user_id'] = 3
        response =self.test_client.delete('/api/v1/users/1', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    
    def test_update_email_error(self):
        self.user['email'] = "ann@gmail.com"
        response = self.test_client.patch('/api/v1/users/1/email', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)
        self.assertTrue({'email will soon be updated','message'},True)

        


if __name__== '__main__':
 unittest.main()


