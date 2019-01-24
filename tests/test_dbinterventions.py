import json
from tests.test_base import BaseTests
from api.secure.safe import encode_token
  
class TestEndpoints(BaseTests):
    
    # def test_get_all_interventions(self):
    #     # response = self.test_client.get(
    #     #     '/api/v2/interventions',
    #     #     headers={'Authorization': encode_token(2)},
    #     #     content_type='application/json')
    #     # data = json.loads(response.data.decode())
        
    #     # self.assertEqual(data,200)
    #     # self.assertTrue(json.loads(data),message )
        
    #     self.assertEqual(encode_token(2).decode('utf-8')



    def test_post_intervention_records(self):
        response = self.test_client.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        
        auth = json.loads(response.data.decode())
        response2 = self.test_client.post(
            '/api/v2/interventions',
            headers={'Authorization': auth['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        result = json.loads(response.data.decode())
        self.assertEqual(201,response.status_code)
        self.assertTrue(result["message"] == "Created intervention record")
        self.assertIsInstance(self.intervention,dict)

        

#     def test_get_specific_intervention_with_id(self):
#         response = self.test_client.post(
#             'api/v2/auth/signup',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         auth = json.loads(response.data.decode())
#         response = self.test_client.get(
#             '/api/v2/interventions/1',
#             headers={'Authorization': auth['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(200,response.status_code)
        


#     def test_update_intervention_record_location_with_id(self):

#         change_intervention_location = {
#                    'location' :'lira'
#                 }

#         self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
#         response = self.test_client.patch('/api/v1/interventions/1/location', content_type= 'application/json', 
#                                    data = json.dumps(change_intervention_location))
#         res = json.loads(response.data.decode())
#         self.assertEqual(200,response.status_code)
        

#     def test_update_intervention_comment_with_id(self):
                
#         change_intervention_comment = {
#                                            'comment':'that is great'
#                                         }  

#         self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
#         response = self.test_client.patch('/api/v1/interventions/1/comment', content_type= 'application/json', 
#                                        data = json.dumps(change_intervention_comment))
#         res = json.loads(response.data.decode())
#         self.assertEqual(200,response.status_code)


#     def test_delete_specific_intervention_with_id(self):
#         self.test_client.post('/api/v2/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
#         response = self.test_client.delete('/api/v2/interventions/1')
#         self.assertEqual(200,response.status_code)
#         self.assertEqual(len(self.intervention),8)


#     def test_status_integer_error(self):
#        response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#        authenticate = json.loads(response.data.decode())
#        self.intervention["status"] = 123
#        response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': authenticate['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#        result = json.loads(response.data.decode())
#        self.assertEqual(400,response.status_code)
#        self.assertTrue(result["error"] ==
#                         "Status must be a string.")

#     def test_empty_status_error(self):
#           response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#           authenticate = json.loads(response.data.decode())
#           self.intervention["status"] = " "
#           response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': authenticate['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#           result = json.loads(response.data.decode())
#           self.assertEqual(400,response.status_code)
#           self.assertTrue(result["error"] ==
#                         "status is required")


#     def test_empty_createdby_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         authenticate = json.loads(response.data.decode())
#         self.intervention["created_by"] = " "
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': authenticate['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "required field is missing")


#     def test_createdby_string_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         auth = json.loads(response.data.decode())
#         self.intervention["created_by"] = "yasin "
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': auth['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertTrue(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "created_by must be an integer")

#     def test_incident_type_integer_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         auth = json.loads(response.data.decode())
#         self.intervention["incident_type"] = 123
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': auth['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "incident type must be a string")
      
#     def test_empty_incident_type_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         auth = json.loads(response.data.decode())
#         self.intervention["incident_type"] = " "
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': auth['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertTrue(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "incident_type is required")

#     def test_comment_integer_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         authenticate = json.loads(response.data.decode())
#         self.intervention["comment"] = 123
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': authenticate['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "comment must be a string")

#     def test_empty_comment_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         auth_token = json.loads(response.data.decode())
#         self.intervention["comment"] = " "
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': auth_token['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "comment is required")

#     def test_empty_location_error(self):
#         response = self.test_client.post(
#             'api/v2/auth/signin',
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )

#         auth_token = json.loads(response.data.decode())
#         self.intervention["location"] = " "
#         response = self.test_client.post(
#             '/api/v2/interventions',
#             headers={'Authorization': auth_token['token']},
#             content_type='application/json',
#             data=json.dumps(self.intervention)
#         )
#         result = json.loads(response.data.decode())
#         self.assertEqual(400,response.status_code)
#         self.assertTrue(result["error"] ==
#                         "location is required")


#     # def test_location_integer_error(self):
#     #     response = self.test_client.post(
#     #         'api/v2/auth/signin',
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )

#     #     auth_token = json.loads(response.data.decode())
#     #     self.intervention["location"] = 123
#     #     response = self.test_client.post(
#     #         '/api/v2/interventions',
#     #         headers={'Authorization': auth_token['token']},
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )
#     #     result = json.loads(response.data.decode())
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue(result["error"] ==
#     #                     "location must be a string")


#     # def test_empty_images_error(self):
#     #     response = self.test_client.post(
#     #         'api/v2/auth/signin',
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )

#     #     auth = json.loads(response.data.decode())
#     #     self.intervention["images"] = " "
#     #     response = self.test_client.post(
#     #         '/api/v2/interventions',
#     #         headers={'Authorization': auth['token']},
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )
#     #     result = json.loads(response.data.decode())
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue(result["error"] ==
#     #                     "invalid! please upload an image")

#     # def test_images_integer_error(self):
#     #     response = self.test_client.post(
#     #         'api/v2/auth/signin',
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )

#     #     auth = json.loads(response.data.decode())
#     #     self.intervention["images"] = 123
#     #     response = self.test_client.post(
#     #         '/api/v2/interventions',
#     #         headers={'Authorization': auth['token']},
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )
#     #     result = json.loads(response.data.decode())
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue(result["error"] ==
#     #                     "images must be a url string")
                        
                        
#     # def test_empty_video_error(self):
#     #     response = self.test_client.post(
#     #         'api/v2/auth/signin',
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )

#     #     auth = json.loads(response.data.decode())
#     #     self.intervention["videos"] = " "
#     #     response = self.test_client.post(
#     #         '/api/v2/interventions',
#     #         headers={'Authorization': auth['token']},
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )
#     #     result = json.loads(response.data.decode())
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue(result["error"] ==
#     #                     "invalid! please upload a video")


#     # def test_video_integer_error(self):
#     #     response = self.test_client.post(
#     #         'api/v2/auth/signin',
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )

#     #     auth_token = json.loads(response.data.decode())
#     #     self.intervention["videos"] = 123
#     #     response = self.test_client.post(
#     #         '/api/v2/interventions',
#     #         headers={'Authorization': auth_token['token']},
#     #         content_type='application/json',
#     #         data=json.dumps(self.intervention)
#     #     )
#     #     result = json.loads(response.data.decode())
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue(result["error"] ==
#     #                     "video must be a url string")
                        
#     # def test_update_intervention_comment_error(self):
#     #     self.intervention['comment'] = "no help recieved"
#     #     response = self.test_client.patch('/api/v2/interventions/1/comment', content_type= 'application/json', data = json.dumps(self.intervention))
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue({'do not comment','message'},True)

#     # def test_update_intervention_location_error(self):
#     #     self.intervention['location'] = "78.12.E"
#     #     response = self.test_client.patch('/api/v2/interventions/1/location', content_type= 'application/json', data = json.dumps(self.intervention))
#     #     self.assertEqual(400,response.status_code)
#     #     self.assertTrue({'location has been removed','message'},True)

#     # def test_delete_specific_intervention_error(self):
#     #     self.intervention['user_id'] = 5
#     #     response =self.test_client.delete('/api/v2/interventions/1', content_type= 'application/json', data = json.dumps(self.intervention))
#     #     self.assertEqual(400,response.status_code)
 




