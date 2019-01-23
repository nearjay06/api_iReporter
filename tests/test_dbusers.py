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

    # def test_get_all_users(self):

    #     response = self.test_client.post(
    #                'api/v2/auth/signup',content_type='application/json',
    #                data=json.dumps(self.user))
	#     authenticate = json.loads(response.data.decode())
	#     response = self.test_client.get('/api/v2/auth/users',
	# 	           headers={'Authorization': authenticate['generated_token']},
	# 	            content_type='application/json',
	# 	           data=json.dumps(self.user)
    #     )
	#     result = json.loads(response.data.decode())
	#     self.assertTrue(201,response.status_code)

	

    
    
    # def test_user_signup(self):
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json',
    #                                      data = json.dumps(self.user))
    #     self.assertEqual(201,response.status_code)
    #     self.assertTrue({'user id is required and it should be an integer','message'},True)
    #     self.assertEqual(len(self.user),9)

    # def test_admin_signup(self):
    #     response = self.test_client.post('/api/v2/auth/admins/signup', content_type= 'application/json',
    #                               data = json.dumps(self.user))
    #     self.assertEqual(201,response.status_code)
    #     self.assertTrue({'user id is required and it should be an integer','message'},True)
    #     self.assertEqual(len(self.user),9)


    def test_user_signin(self):
        items={
            "password":"lalaland",
            "username": "trickster"
                       
            }

        response = self.test_client.post('/api/v2/auth/signin', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(200,response.status_code)
        self.assertTrue({'created user','message'},True)
           
       
    def test_empty_firstname_error(self):
        self.user["first_name"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)
    
    def test_firstname_integer_error(self):
        self.user["first_name"] = 123
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_lastname_error(self):
         self.user["last_name"] = " "
         response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
         self.assertEqual(400,response.status_code)

    def test_lastname_integer_error(self):
        self.user["last_name"] = 456
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_othernames_error(self):
        self.user["other_names"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_othernames_integer_error(self):
        self.user["other_names"] = 123
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_email_error(self):
        self.user["email"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_email_integer_error(self):
        self.user["email"] = 123456
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_email_syntax_error(self):
        self.user["email"] = "joangmail"
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_password_error(self):
        self.user["password"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_password_integer_error(self):
        self.user["password"] = 123456
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_password_length_error(self):
        self.user["password"] = "abcdefghijklmnopqrst"
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_username_integer_error(self):
        self.user["username"] = 1234
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_username_error(self):
        self.user["username"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    def test_empty_phonenumber_error(self):
        self.user["phone_number"] = " "
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)
    
    def test_phonenumber_integer_error(self):
        self.user["phone_number"] = 345678
        response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
        self.assertEqual(400,response.status_code)

    

        


if __name__== '__main__':
 unittest.main()


