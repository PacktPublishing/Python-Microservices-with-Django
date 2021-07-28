from django.test import TestCase
from app01.models import Employee as emp
from django.core import serializers

# Writing the class for unit testing.
class AppTest(TestCase):

    # Check function to validate the URL.
    def test_url(self):
    	url_response = self.client.get('http://127.0.0.1:8000/get_data/emp_details/?employee_id=2')
    	self.assertEqual(url_response.status_code, 200)

    # To check with invalid urls.
    def test_invalid_url(self):
    	url_response = self.client.get('http://127.0.0.1:8000/get_data/emp/')
    	self.assertEqual(url_response.status_code, 404)

    # To validate the invalid data.
    def test_invalid_data(self):
        query_output = serializers.serialize('json', emp.objects.filter(employee_id= 4))
        resp = '[]'
        self.assertEqual(query_output, resp)