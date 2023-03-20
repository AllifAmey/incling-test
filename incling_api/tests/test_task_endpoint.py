from django.test import TestCase
from rest_framework.test import APIClient
import json
from incling_api import models



class TestTaskEndpoint(TestCase):
    
    
    def test_list_get_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
    
    def test_retrieve_get_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
    
    def test_post_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
    
    def test_post_validation_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
    
    def test_put_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')
        
    def test_delete_request(self):
        """
        Basic test for GET request of flood API.
        """
        client = APIClient()
        models.Tile.objects.create(launch_date="2023-03-20", status="archived")
        res = client.get("/api/tile/", format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), '[{"id": 1, "launch_date": "2023-03-20", "status": "archived"}]')

    
    
    