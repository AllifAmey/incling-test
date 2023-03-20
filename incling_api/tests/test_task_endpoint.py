from django.test import TestCase
from rest_framework.test import APIClient
import json
from incling_api import models



class TestTaskEndpoint(TestCase):
    
    
    def testing_setup(self):
        
        client = APIClient()
        tile = models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        return [client, tile]
    
    def test_list_get_request(self):
        """
        Basic test for GET request ( list viewset method ) of Task API.
        """
        client, tile = self.testing_setup()
        models.Task.objects.create(tile=tile, 
                                   title="Art", 
                                   order="Draw", 
                                   type="survey", 
                                   description="Art Lesson")
        res = client.get("/api/task/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"}]')
    
    def test_retrieve_get_request(self):
        """
        Basic test for GET request ( retrieve viewset method ) of Task API.
        """
        client, tile = self.testing_setup()
        models.Task.objects.create(tile=tile, 
                                   title="Art", 
                                   order="Draw", 
                                   type="survey", 
                                   description="Art Lesson")
        res = client.get("/api/task/1/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"}')
    
    def test_post_request(self):
        """
        Basic test for POST request of Task API.
        """
        client, tile = self.testing_setup()
        res = client.post("/api/task/", {"tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"}')
    
    def test_post_validation_request(self):
        """
        Test for POST request of Task API - validation
        """
        client, tile = self.testing_setup()
        res = client.post("/api/task/", {"tile": 1, "title": "Art", "order": "Draw", "type": "surveyy", "description": "Art Lesson"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.dumps(res.data), '{"type": ["Status must be survey, discussion or diary"]}')
    
    def test_put_request(self):
        """
        Basic test for PUT request of Task API.
        """
        client, tile = self.testing_setup()
        res = client.post("/api/task/", {"tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"})
        res = client.put("/api/task/1/", {"tile": 1, "title": "Art", "order": "Drawing", "type": "survey", "description": "Art Lesson"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "tile": 1, "title": "Art", "order": "Drawing", "type": "survey", "description": "Art Lesson"}')
    
    def test_put_validation_request(self):
        """
        Test for PUT request of Task API. - validation
        """
        client, tile = self.testing_setup()
        res = client.post("/api/task/", {"tile": 1, "title": "Art", "order": "Draw", "type": "survey", "description": "Art Lesson"})
        res = client.put("/api/task/1/", {"tile": 1, "title": "Art", "order": "Drawing", "type": "surveyy", "description": "Art Lesson"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.dumps(res.data), '{"type": ["Status must be survey, discussion or diary"]}')
        
    def test_delete_request(self):
        """
        Basic test for DELETE request of Task API.
        """
        client, tile = self.testing_setup()
        models.Task.objects.create(tile=tile, 
                                   title="Art", 
                                   order="Draw", 
                                   type="survey", 
                                   description="Art Lesson")
        res = client.delete("/api/tile/1/", format="json")
        self.assertEqual(res.status_code, 204)

    
    
    