from django.test import TestCase

# Create your tests here.

class HelloWorldTestCase(TestCase):

    def test_hello_world(self):

        response = self.client.get('Hello World!')
