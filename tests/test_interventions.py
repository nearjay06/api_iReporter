import unittest
from api.routes.intervention_endpoints import app
from api.models.incident import Incidents, Interventions, interventions_list
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = app.test_client()
        self.intervention = {
                "comment": "blaj",
                "created_by": 456,
                "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
                "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
                "incident_type": "intervention",
                "location": "karamoja",
                "status": "under investigation",
                "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
                                                       
                }

    def tearDown(self):
         interventions_list.clear()

    def test_get_all_interventions(self):
        self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
        response = self.test_client.get('/api/v1/interventions')
        self.assertEqual(200,response.status_code)
        self.assertNotIsInstance('location',Interventions,"message")
    

    def test_post_intervention_records(self):
        response = self.test_client.post('/api/v1/interventions', content_type= 'application/json',
                                  data = json.dumps(self.intervention))
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(self.intervention,dict)
        self.assertTrue({'created intervention record','message'},True)
    

    def test_get_specific_intervention_with_id(self):
        self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
        response = self.test_client.get('/api/v1/interventions/1')
        self.assertEqual(200,response.status_code)
        self.assertTrue({'intervention is in the list','message'},True)


    def test_update_intervention_record_location_with_id(self):

        change_intervention_location = {
                   'location' :'lira'
                }

        self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
        response = self.test_client.patch('/api/v1/interventions/1/location', content_type= 'application/json', 
                                   data = json.dumps(change_intervention_location))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        

    def test_update_intervention_comment_with_id(self):
                
        change_intervention_comment = {
                                           'comment':'that is great'
                                        }  

        self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
        response = self.test_client.patch('/api/v1/interventions/1/comment', content_type= 'application/json', 
                                       data = json.dumps(change_intervention_comment))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)


    def test_delete_specific_intervention_with_id(self):
        self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
        response = self.test_client.delete('/api/v1/interventions/1')
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(self.intervention),8)


    # def test_status_integer_error(self):
    #     self.intervention["status"] = 1234
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_incident_type_error(self):
    #     self.intervention["incident_type"] = " "
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_comment_integer_error(self):
    #     self.intervention["comment"] = 123
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_location_error(self):
    #     self.redflag["location"] = " "
    #     response = self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_images_error(self):
    #     self.intervention["images"] = " "
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_comment_error(self):
    #     self.intervention["comment"] = " "
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_video_error(self):
    #     self.intervention["videos"] = " "
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_location_error(self):
    #     self.intervention["location"] = " "
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)
   
    # def test_empty_incident_type_integer_error(self):
    #     self.intervention["incident_type"] = 5678
    #     response = self.test_client.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(self.intervention))
    #     self.assertEqual(400,response.status_code)













if __name__== '__main__':
 unittest.main()


