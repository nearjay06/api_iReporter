import json
from tests.test_base import BaseTests 
from api.secure.safe import encode_token



class TestEndpoints(BaseTests):

                                    
    def test_get_all_redflag_records(self):
        response = self.test_client.post(
            '/api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )
        auth = json.loads(response.data.decode())
        response2 = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )

        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(self.redflag),8) 
         

    def test_post_redflag_records(self):
        response = self.test_client.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )
        
        auth = json.loads(response.data.decode())
        response2 = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
          
        self.assertEqual(201,response.status_code)
        self.assertTrue(result["message"] == "Created redflag record")
        self.assertIsInstance(self.redflag,dict)
        self.assertTrue({'incident id must not be a string','message'},True)
    
        
    def test_get_specific_redflag_with_id(self):
        response = self.test_client.post(
            '/api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.signin)
        )
        
        auth = json.loads(response.data.decode())
        response2 = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(self.redflag,dict)    
        

    def test_update_redflag_record_location(self):
        response = self.test_client.post(
            '/api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        
        auth = json.loads(response.data.decode("sub",('utf-8')))
        response = self.test_client.patch(
            '/api/v2/redflags/1/location',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertTrue(result["message"] == "updated redflag location")
        
                      

    def test_edit_redflag_record_comment(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )
        
        auth = json.loads(response.data.decode())
        response = self.test_client.patch(
            '/api/v2/redflags/1/comment',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        self.assertEqual(200,response.status_code)
        self.assertTrue(response["message"] == "updated redflag location")
         


    def test_delete_redflag_record_with_id(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )
        
        auth = json.loads(response.data.decode("sub",('utf-8')))
        response = self.test_client.delete(
            '/api/v2/redflags/1',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(self.intervention),8)
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        self.assertIsInstance(self.redflag,dict)

    def test_empty_status_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        authenticate = json.loads(response.data.decode())
        self.intervention["status"] = " "
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "status is required")


    def test_status_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        authenticate = json.loads(response.data.decode())
        self.redflag["status"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "Status must be a string.")


    def test_createdby_string_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth = json.loads(response.data.decode())
        self.redflag["created_by"] = "yasin "
        response = self.test_client.post(
            '/api/v2/redflag',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertTrue(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "created_by must be an integer")

    def test_empty_createdby_error(self):
       response = self.test_client.post(
            'api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.user)
        )

       authenticate = json.loads(response.data.decode())
       self.redflag["created_by"] = " "
       response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
       result = json.loads(response.data.decode())
       self.assertEqual(400,response.status_code)
       self.assertTrue(result["error"] ==
                        "required field is missing")


    def test_empty_location_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["location"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "location is required")



    def test_location_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["location"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "location must be a string")


    def test_empty_comment_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["comment"] = " "
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "comment is required")


    def test_comment_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        authenticate = json.loads(response.data.decode())
        self.intervention["comment"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "comment must be a string")


    def test_location_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["location"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "location must be a string")

    
    def test_redflag_location_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["location"] = " "
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "location is required")

    def test_empty_videos_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth = json.loads(response.data.decode())
        self.intervention["videos"] = " "
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "invalid! please upload a video")


    def test_videos_integer_error(self):
        response = self.test_client.post(
            'api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth_token = json.loads(response.data.decode())
        self.redflag["videos"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "video must be a url string")


    def test_empty_incident_type_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth = json.loads(response.data.decode())
        self.intervention["incident_type"] = " "
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertTrue(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "incident_type is required")

    def test_incident_type_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth = json.loads(response.data.decode())
        self.redflag["incident_type"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "incident type must be a string")


    def test_empty_images_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth = json.loads(response.data.decode())
        self.redflag["images"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "invalid! please upload an image")


    def test_images_integer_error(self):
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.signin)
        )

        auth = json.loads(response.data.decode())
        self.intervention["images"] = 123
        response = self.test_client.post(
            '/api/v2/redflags',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["error"] ==
                        "images must be a url string")



#     def test_update_location_error(self):
            
#         self.redflag['location'] = "12.34.N"
#         response = self.test_client.patch('/api/v2/redflags/1/location', content_type= 'application/json', data = json.dumps(self.redflag))
#         self.assertEqual(400,response.status_code)
#         self.assertTrue({'location verified','message'},True)

#     def test_update_redflag_comment_error(self):
#         self.redflag['comment'] = "unlike"
#         response = self.test_client.patch('/api/v2/redflags/1/comment', content_type= 'application/json', data = json.dumps(self.redflag))
#         self.assertEqual(400,response.status_code)
#         self.assertTrue({'do not comment','message'},True)

#     def test_delete_specific_redflag_error(self):
#         self.redflag['user_id'] = 3
#         response =self.test_client.delete('/api/v2/redflags/1', content_type= 'application/json', data = json.dumps(self.redflag))
#         self.assertEqual(400,response.status_code)
 
      
      





