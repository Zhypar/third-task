from rest_framework.test import APITestCase
from .models import *



class TestCourse(APITestCase):
    url = '/api/courses/'
    url2 = '/api/courses/?id=7/'
    url3 = '/api/courses/?id=7'


    def test_get_courses(self):

        Course.objects.create(id=7, name="Swimming", logo = "image")
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], "Swimming")

    def test_get_a_course(self):

        Course.objects.create(id=7, name="Swimming", logo = "image")
        response = self.client.get(self.url2)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], "Swimming")

    def test_post_a_course(self):

        contact = Contact.objects.create(
                    type= "1",
                    value = "89898989")
        branch = Branch.objects.create(
                    latitude= 1,
                    longtitude= 2,
                    address = "Mira")
        category = Category.objects.create(
                    name= "Music",
                    imgpath= "img"
        )

        Course.objects.create(category= category, contacts= contact, branches=branch)

        data = {
            "id": 8,
            "name": "Piano",
            "description": "text",
            "category": 1,
            "logo": "image",
            "contacts": [{
                "type": "1",
                "value": "89898989"}],
            "branches": [{
                "latitude": 1,
                "longtitude": 2,
                "address": "Mira"}]
        }
        response = self.client.post(self.url, data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)

    def test_delete_a_course(self):

        Course.objects.create(id=7, name="Swimming", logo = "image")
        response = self.client.delete(self.url3)
        self.assertEqual(response.status_code, 204)