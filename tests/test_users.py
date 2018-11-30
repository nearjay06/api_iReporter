import unittest
from api.routes.user_endpoints import app
from api.models.user import Users
from api.validations import user_valid

import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

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
            "username": "trickster"
        }

        self.app.post('/api/v1/users', content_type= 'application/json', data = json.dumps(items))
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code,200)
        



    def test_post_user_record(self):
        response = self.app.post('/api/v1/users')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.content_type,'application/json')
        self.assertTrue({'user id is required and it should be an integer','message'},True)

    def test_post_user_record_returns_errors(self):
        response = self.app.post ('/api/v1/users',
                    data=json.dumps( {'user_id':"iiii",
                                      "first_name": "abcd",
                                      "last_name":"joan",
                                      "other_names":"mermaid",
                                      "email": "joan@gmail.com",
                                      "phone_number":"abcdefg",
                                      "username": "lethal",
                                      "registered":"12/11/2018",
                                      "isAdmin":"True"
                                         
                                      }
                                    ),
                    content_type='application/json')
                        
        self.assertEqual(response.status_code,401)
        content=response.get_json()
        print(content)


    def test_get_user_with_id(self):
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertIsInstance('user_id',Users,"message")

    def test_update_phone_number_with_user_id(self):
        response = self.app.patch('/api/v1/users/<int:user_id>/phone_number')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertTrue("phone number has been updated","message",True)

    def test_update_user_email_with_id(self):
        response = self.app.patch('/api/v1/users/<int:user_id>/email')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertFalse("user is in the list","message",False)

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
            "username": "trickster"
        }

        self.app.post('/api/v1/users', content_type= 'application/json', data = json.dumps(items))
        response = self.app.delete('/api/v1/users/<int:incident_id>')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')













if __name__== '__main__':
 unittest.main()