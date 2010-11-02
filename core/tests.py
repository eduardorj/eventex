from django.test import TestCase

class HomePageUrlTest(TestCase):
	# fixtures = ['initial_data.js']
	
	def setUp(self):
		pass
	
	def tearDown(self):
		pass

	def test_success_when_get_homepage(self):
		response = self.client.get('/')
		self.assertEquals(200, response.status_code)
		self.assertTemplateUsed(response, 'index.html') 

