import unittest
from api.routes.intervention_endpoints import app
from api.models.incident import Incidents, Interventions
from api.validations import valid

import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

def test_get_all_interventions(self):
    response = self.app.get('/api/v1/interventions')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.content_type,'application/json')
    self.assertIsInstance('location',Interventions,"message")
    

def test_post_intervention_records(self):
    response = self.app.post('/api/v1/interventions')
    self.assertEqual(response.status_code,201)
    self.assertEqual(response.content_type,'application/json')
    self.assertFalse({'comment has been updated','message'},False)
    

def test_get_specific_intervention_with_id(self):
    response = self.app.get('/api/v1/interventions/1')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.content_type,'application/json')
    self.assertTrue({'intervention is in the list','message'},True)


def test_update_intervention_record_location_with_id(self):
    response = self.app.patch('/api/v1/interventions/1/location')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.content_type,'application/json')


def test_update_intervention_comment_with_id(self):
    response = self.app.patch('/api/v1/interventions/1/comment')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.content_type,'application/json')


def test_delete_specific_intervention_with_id(self):
    response = self.app.delete('/api/v1/interventions/1')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.content_type,'application/json')






















if __name__== '__main__':
 unittest.main()