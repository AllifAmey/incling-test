from django.test import TestCase
from rest_framework.test import APIClient
import json
from incling_api import models



class TestTileEndpoint(TestCase):
    
    
    def test_list_get_request(self):
        """
        Basic test for GET request ( list viewset method ) of Tile API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
    
    def test_retrieve_get_request(self):
        """
        Basic test for GET request ( retrieve viewset method ) of Tile API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/1/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "launch_date": "2023-03-20", "status": "archived"}')
    
    def test_post_request(self):
        """
        Basic test for POST request of Tile API.
        """
        client = APIClient()
        res = client.post("/api/tile/", {"launch_date": "2023-03-20","status": "archived"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "launch_date": "2023-03-20", "status": "archived"}')
    
    def test_post_validation_request(self):
        """
        Test for POST request of Tile API  - validation
        """
        client = APIClient()
        res = client.post("/api/tile/", {"launch_date": "2023-03-20","status": "archivedd"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.dumps(res.data), '{"status": ["Status must be live, pending or archived"]}')
    
    def test_put_request(self):
        """
        Basic test for PUT request of Tile API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.put("/api/tile/1/", {"launch_date": "2023-03-20","status": "live"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '{"id": 1, "launch_date": "2023-03-20", "status": "live"}')
    
    def test_put_validation_request(self):
        """
        Test for PUT request of Tile API - validation
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.put("/api/tile/1/", {"launch_date": "2023-03-20","status": "livee"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.dumps(res.data), '{"status": ["Status must be live, pending or archived"]}')
        
    def test_delete_request(self):
        """
        Basic test for DELETE request of Tile API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.delete("/api/tile/1/",)
        self.assertEqual(res.status_code, 204)

    
    
    