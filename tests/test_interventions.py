import unittest
from api.routes.intervention_endpoints import app
from api.models.incident import Incidents, Interventions, interventions_list
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        interventions_list.clear()

    def test_get_all_interventions(self):
        data = {
                 "comment": "blaj",
                 "created_by": 456,
                 "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
                 "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
                 "incident_type": "intervention",
                 "location": "karamoja",
                 "status": "under investigation",
                 "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
       
                }

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/interventions')
        self.assertEqual(200,response.status_code)
        self.assertNotIsInstance('location',Interventions,"message")
    

    def test_post_intervention_records(self):
        data = {
              "comment": "blaj",
              "created_by": 789,
              "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
              "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
              "incident_type": "intervention",
              "location": "karamoja",
              "status": "under investigation",
              "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"

            }

        response = self.app.post('/api/v1/interventions', content_type= 'application/json',
                                  data = json.dumps(data))
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(data,dict)
        self.assertTrue({'created intervention record','message'},True)
    

    def test_get_specific_intervention_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": 678,
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
            
            }  
        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/interventions/1')
        self.assertEqual(200,response.status_code)
        self.assertTrue({'intervention is in the list','message'},True)


    def test_update_intervention_record_location_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": 6789,
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
            
            }  

        change_intervention_location = {
                   'location' :'lira'
                }

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.patch('/api/v1/interventions/1/location', content_type= 'application/json', 
                                   data = json.dumps(change_intervention_location))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        

    def test_update_intervention_comment_with_id(self):
        data = {
                 "comment": "blaj",
                 "created_by": 456,
                 "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
                 "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
                 "incident_type": "intervention",
                 "location": "karamoja",
                "status": "under investigation",
                 "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
                
                }
                
        change_intervention_comment = {
                                           'comment':'that is great'
                                        }  

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.patch('/api/v1/interventions/1/comment', content_type= 'application/json', 
                                       data = json.dumps(change_intervention_comment))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)



    def test_delete_specific_intervention_with_id(self):
        data = {
            "comment": "blaj",
            "created_by": 678,
            "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
            "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
            "incident_type": "intervention",
            "location": "karamoja",
            "status": "under investigation",
            "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"


            }

        self.app.post('/api/v1/interventions', content_type= 'application/json', data = json.dumps(data))
        response = self.app.delete('/api/v1/interventions/1')
        self.assertEqual(200,response.status_code)
        self.assertEqual(len(data),8)




if __name__== '__main__':
 unittest.main()