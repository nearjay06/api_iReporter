import unittest
from api.routes.intervention_endpoints import app
from api.models.incident import Incidents, Interventions,interventions_list
from api.controllers import control
from api.validations import valid

import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        interventions_list.clear()

    def test_get_all_interventions(self):
        data = {
                 "comment": "blaj",
                 "created_by": "tatatat",
                 "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
                 "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
                 "incident_id": 2,
                 "incident_type": "intervention",
                 "location": "karamoja",
                 "status": "under investigation",
                 "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
       
                }

        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/interventions')
        self.assertEqual(response.status_code,200)
        self.assertNotIsInstance('location',Interventions,"message")
    

    def test_post_intervention_records(self):
        data = {
            "comment": "blaj",
            "created_by": "tatatat",
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_id": 2,
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"

            }

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.post('/api/v1/interventions')
        self.assertEqual(response.status_code,201)
        self.assertIsInstance(data,dict)
        self.assertFalse({'comment has been updated','message'},False)
    

    def test_get_specific_intervention_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": "tatatat",
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_id": 2,
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
            
            }  
        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/interventions/1')
        self.assertEqual(response.status_code,200)
        self.assertTrue({'intervention is in the list','message'},True)


    def test_update_intervention_record_location_with_id(self):
        response = self.app.patch('/api/v1/interventions/1/location')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')


    def test_update_intervention_comment_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": "tatatat",
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_id": 2,
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
            
            }  

        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.patch('/api/v1/interventions/1/comment')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')


    def test_delete_specific_intervention_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": "tatatat",
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_id": 2,
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"


            }

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.delete('/api/v1/interventions/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(data),9)






















if __name__== '__main__':
 unittest.main()