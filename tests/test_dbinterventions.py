import json
from tests.test_base import BaseTests
from api.secure.safe import encode_token
  
class TestEndpoints(BaseTests):
    
    def test_get_all_interventions(self):
        response = self.test_client.post(
            '/api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.credentials)
        )
        auth = json.loads(response.data.decode())
        response2 = self.test_client.get(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )

        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(self.intervention),8) 

    def test_post_intervention_records(self):
        self.test_client.post('/api/v2/auth/signup',content_type='application/json',
                          data=json.dumps(self.user)
                      )

        response = self.test_client.post(
            '/api/v2/auth/signin',content_type='application/json',
            data=json.dumps(self.credentials)
             )
             
        auth = json.loads(response.data.decode())
        response = self.test_client.post('/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(201,response.status_code)
        self.assertTrue(result["message"] == "Created intervention record")
        self.assertIsInstance(self.intervention,dict)

        
    def test_get_specific_intervention_with_id(self):
        self.test_client.post(
            '/api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.credentials)
        )        
        auth = json.loads(response.data.decode())
        self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )

        auth = json.loads(response.data.decode())
        response = self.test_client.get(
            '/api/v2/interventions/1',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(self.intervention,dict)    
               
    def test_update_intervention_record_location_with_id(self):
        self.test_client.post(
                             '/api/v2/auth/signup', content_type='application/json',
                              data=json.dumps(self.user)
                            )
        response = self.test_client.post('/api/v2/auth/signin', content_type ='application/json',
                          data=json.dumps(self.credentials))
        
        self.test_client.post(
                             '/api/v2/interventions', content_type='application/json',
                              data=json.dumps(self.intervention)
                            )
        auth = json.loads(response.data.decode())
        response = self.test_client.patch(
            '/api/v2/interventions/1/location',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertTrue(result["message"] == "updated intervention record location")
        

    def test_update_intervention_comment_with_id(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                              data=json.dumps(self.user)
                         )

        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                              data=json.dumps(self.credentials)
                         )

        self.test_client.post('/api/v2/interventions', content_type='application/json',
                              data=json.dumps(self.intervention)
                         )
                                   
        auth = json.loads(response.data.decode())
        response = self.test_client.patch(
            '/api/v2/interventions/1/comment',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertTrue(result["message"] == "updated intervention record comment")
                
 
    def test_delete_specific_intervention_with_id(self):
        self.test_client.post('/api/v2/auth/signup',content_type='application/json',
                              data=json.dumps(self.user)
                        )
        
        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                              data=json.dumps(self.credentials)
                         )

        self.test_client.post('/api/v2/interventions', content_type='application/json',
                              data=json.dumps(self.intervention)
                         )
                         
        auth = json.loads(response.data.decode())
        response = self.test_client.delete( '/api/v2/interventions/1',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(self.intervention),8)


    def test_status_integer_error(self):
       self.test_client.post('/api/v2/auth/signup',content_type='application/json',
                             data=json.dumps(self.user)
                )
       response = self.test_client.post('/api/v2/auth/signin',content_type='application/json',
                             data=json.dumps(self.credentials)
                )

       authenticate = json.loads(response.data.decode())
       self.intervention["status"] = 123
       response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
       result = json.loads(response.data.decode())
       self.assertEqual(400,response.status_code)
       self.assertTrue(result["message"] == "status must be a string")

    def test_empty_status_error(self):
        self.test_client.post( '/api/v2/auth/signup',content_type='application/json',
                            data=json.dumps(self.user)
                     )

        response = response = self.test_client.post( '/api/v2/auth/signin',
                              content_type='application/json',
                              data=json.dumps(self.credentials)
                    )

        authenticate = json.loads(response.data.decode())
        self.intervention["status"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "status is required")

    def test_empty_createdby_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                            data=json.dumps(self.user)
                     )

        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.credentials)
        )

        authenticate = json.loads(response.data.decode())
        self.intervention["created_by"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "created_by must be an integer")


    def test_createdby_string_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                         data=json.dumps(self.user)
                     )

        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                         data=json.dumps(self.user)
                     )

        auth = json.loads(response.data.decode())
        self.intervention["created_by"] = "yasin "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertTrue(400,response.status_code)
        self.assertTrue(result["message"] =="created_by must be an integer")

    def test_incident_type_integer_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                             data=json.dumps(self.user)
                    )
        response = self.test_client.post( '/api/v2/auth/signin',content_type='application/json',
                             data=json.dumps(self.credentials)
                   )

        auth = json.loads(response.data.decode())
        self.intervention["incident_type"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] =="incident type must be a string")
      
    def test_empty_incident_type_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                               data=json.dumps(self.user)
                    )
        response = self.test_client.post(
            '/api/v2/auth/signin', content_type='application/json',
                   data=json.dumps(self.credentials)
             )

        auth = json.loads(response.data.decode())
        self.intervention["incident_type"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertTrue(400,response.status_code)
        self.assertTrue(result["message"] == "incident type is required")

    def test_comment_integer_error(self):
        self.test_client.post( '/api/v2/auth/signup', content_type='application/json',
                             data=json.dumps(self.user)
                         )
        response = self.test_client.post(
            '/api/v2/auth/signin',
            content_type='application/json',
            data=json.dumps(self.credentials)
        )

        authenticate = json.loads(response.data.decode())
        self.intervention["comment"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': authenticate['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "comment must be a string")

    def test_empty_comment_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                             data=json.dumps(self.user)
                         )
        
        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                         data=json.dumps(self.credentials)
                   )

        auth_token = json.loads(response.data.decode())
        self.intervention["comment"] = " "
        
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "comment is required")

    def test_empty_location_error(self):
        self.test_client.post( '/api/v2/auth/signup', content_type='application/json',
                            data=json.dumps(self.user)
                      )

        response = self.test_client.post( '/api/v2/auth/signin', content_type='application/json',
                         data=json.dumps(self.credentials)
                 )

        auth_token = json.loads(response.data.decode())
        self.intervention["location"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "location is required")


    def test_location_integer_error(self):
        self.test_client.post('/api/v2/auth/signup',content_type='application/json',
                        data=json.dumps(self.user)
                      )

        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                           data=json.dumps(self.credentials)
                 )

        auth_token = json.loads(response.data.decode())
        self.intervention["location"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "location must be a string")


    def test_empty_images_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                           data=json.dumps(self.user)
                        )

        response = self.test_client.post( '/api/v2/auth/signin', content_type='application/json',
            data=json.dumps(self.credentials)
               )

        auth = json.loads(response.data.decode())
        self.intervention["images"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "invalid! please upload an image")

    def test_images_integer_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                            data=json.dumps(self.user)
                )

        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                         data=json.dumps(self.credentials)
                     )

        auth = json.loads(response.data.decode())
        self.intervention["images"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertFalse(result["message"] == "images must be a url string")
                        
    def test_empty_video_error(self):
        self.test_client.post('/api/v2/auth/signup', content_type='application/json',
                          data=json.dumps(self.user)
                    )
        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
            data=json.dumps(self.credentials)
              )

        auth = json.loads(response.data.decode())
        self.intervention["videos"] = " "
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "invalid! please upload a video")

    def test_video_integer_error(self):
        self.test_client.post( '/api/v2/auth/signup', content_type='application/json',
                              data=json.dumps(self.user)
                 )

        response = self.test_client.post('/api/v2/auth/signin', content_type='application/json',
                      data=json.dumps(self.credentials)
           )

        auth_token = json.loads(response.data.decode())
        self.intervention["videos"] = 123
        response = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(400,response.status_code)
        self.assertTrue(result["message"] == "video must be a url string")
                      
   