import unittest
from api.routes.user_endpoints import app
from api.models.user import Users,user_list,Admin,admin_access
from api.validations import user_valid

import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        user_list.clear()
    
    def test_get_all_users(self):
        items={
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

        self.app.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(items))
        response = self.app.get('/api/v1/users')
        self.assertEqual(200,response.status_code)
        
    def test_user_signup(self):
        items={
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

        response = self.app.post('/api/v1/users/signup', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'user id is required and it should be an integer','message'},True)
        self.assertEqual(len(items),9)

    def test_admin_signup(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": True,
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "password":"lalaland",
            "username": "trickster"
            
            }

        response = self.app.post('/api/v1/admins/signup', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'user id is required and it should be an integer','message'},True)
        self.assertEqual(len(items),9)


    def test_user_signin(self):
        items={
            "email"            
            : "joan@gmail.com",
            "password":"lalaland",
            "username": "trickster"
                       
            }

        response = self.app.post('/api/v1/users/signin', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(201,response.status_code)
        self.assertTrue({'created user','message'},True)
           
       
    
    def test_get_user_with_id(self):
        items={
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

        self.app.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(items))
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(items,dict)

    def test_update_phone_number_with_user_id(self):
        items={
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


        change_phone_number = {
                               "phone_number":"abcdefg"
                           }

        self.app.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(items))
        response = self.app.patch('/api/v1/users/1/phone_number',
                          content_type= 'application/json',data = json.dumps(change_phone_number))
        self.assertEqual(200,response.status_code)
        res = json.loads(response.data.decode())
        self.assertTrue({'updated phone number ','message'},True) 

    def test_update_user_email_with_id(self):
        items={
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

        change_email = {
                        "email": "new_email@gmail.com"
                       }

        self.app.post('/api/v1/users/signup', content_type= 'application/json',data = json.dumps(items))
        response = self.app.patch('/api/v1/users/1/email',content_type= 'application/json', 
                                   data = json.dumps(change_email))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertTrue({"updated email address","message"},True)

    def test_delete_specific_user_with_id(self):
        items={
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

        self.app.post('/api/v1/users/signup', content_type= 'application/json', data = json.dumps(items))
        response = self.app.delete('/api/v1/users/1')
        self.assertEqual(200,response.status_code)
        
    






if __name__== '__main__':
 unittest.main()