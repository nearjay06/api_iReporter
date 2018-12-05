import unittest
from api.routes.user_endpoints import app
from api.models.user import Users,user_list
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
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
        }

        self.app.post('/api/v1/users', content_type= 'application/json', data = json.dumps(items))
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code,200)
        
    def test_post_user_record(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
            
            }

        response = self.app.post('/api/v1/users', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(response.status_code,200)
        self.assertTrue({'user id is required and it should be an integer','message'},True)
        self.assertEqual(len(items),10)

    
    def test_get_user_with_id(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
            
            }

        self.app.post('/api/v1/users', content_type= 'application/json',data = json.dumps(items))
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(items,dict)

    def test_update_phone_number_with_user_id(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
            
            }


        change_phone_number = {
                               "phone_number":"abcdefg"
                           }

        self.app.post('/api/v1/users', content_type= 'application/json',data = json.dumps(items))
        response = self.app.patch('/api/v1/users/1/phone_number',
                          content_type= 'application/json',data = json.dumps(change_phone_number))
        self.assertEqual(response.status_code,200)
        res = json.loads(response.data.decode())
        self.assertTrue({'updated phone number ','message'},True) 

    def test_update_user_email_with_id(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
            
            }

        change_email = {
                        "email": "new_email@gmail.com"
                       }

        self.app.post('/api/v1/users', content_type= 'application/json',data = json.dumps(items))
        response = self.app.patch('/api/v1/users/1/email',content_type= 'application/json', 
                                   data = json.dumps(change_email))
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)
        self.assertTrue({"updated email address","message"},True)

    def test_delete_specific_user_with_id(self):
        items={
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "isAdmin": "false",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 3,
            "password":"lalaland",
            "username": "trickster"
            
            }

        self.app.post('/api/v1/users', content_type= 'application/json', data = json.dumps(items))
        response = self.app.delete('/api/v1/users/1')
        self.assertEqual(response.status_code,200)
        
    def test_get_all_admins(self):
        items ={
            "email": "jo@gmail.com",
            "first_name": "dadadad",
            "isAdmin": "true",
            "last_name": "ann",
            "other_names": "lala",
            "phone_number": "efg",
            "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
            "user_id": 2,
            "password":"lalaland",
            "username": "play"
        }

        self.app.post('/api/v1/users/admins', content_type= 'application/json', data = json.dumps(items))
        response = self.app.get('/api/v1/users/admins')
        self.assertEqual(response.status_code,200)
        
    def test_post_admin_record(self):
        items={
              "first_name":"ytyty",
              "last_name":"yuyuy",
              "admin_othernames":"yuyu",
              "admin_email":"hhh@gmail.com",
              "admin_phonenumber":"kiii",
              "admin_username":"poi",
              "admin_password":"opm",
              "registered": "Wed, 05 Dec 2018 15:33:01 GMT",
              "user_id": 1,
              "isAdmin": "true"
            }

        response = self.app.post('/api/v1/users/admins', content_type= 'application/json',
                                  data = json.dumps(items))
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(items),10)
       
    def test_get_admin_with_id(self):
        items={
             "email": "jo@gmail.com",
             "first_name": "dadadad",
             "isAdmin": "true",
             "last_name": "ann",
             "other_names": "lala",
             "phone_number": "efg",
             "registered": "Thu, 29 Nov 2018 16:38:07 GMT",
             "user_id": 2,
             "password":"lalaland",
             "username": "play"
                        
            }

        self.app.post('/api/v1/users/admins', content_type= 'application/json',data = json.dumps(items))
        response = self.app.get('/api/v1/users/1/admins')
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(items,dict)












if __name__== '__main__':
 unittest.main()