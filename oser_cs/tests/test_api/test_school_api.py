"""School API tests."""

from rest_framework import status

from tutoring.serializers import SchoolSerializer
from tests.factory import SchoolFactory
from tests.utils.api import HyperlinkedAPITestCase


class SchoolEndpointsTest(HyperlinkedAPITestCase):
    """Test access to the school endpoints."""

    factory = SchoolFactory
    serializer_class = SchoolSerializer

    def test_list(self):
        url = '/api/schools/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        obj = self.factory.create()
        url = '/api/schools/{obj.pk}/'.format(obj=obj)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        url = '/api/schools/'
        obj = self.factory.build()
        data = self.serialize(obj, 'post', url)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=response.data)

    def test_update(self):
        obj = self.factory.create()
        url = '/api/schools/{obj.pk}/'.format(obj=obj)
        data = self.serialize(obj, 'put', url)
        data['name'] = 'Modified name'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=response.data)

    def test_partial_update(self):
        obj = self.factory.create()
        url = '/api/schools/{obj.pk}/'.format(obj=obj)
        data = {'name': 'Modified name'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=response.data)

    def test_delete(self):
        obj = self.factory.create()
        url = '/api/schools/{obj.pk}/'.format(obj=obj)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_tutors(self):
        pass  # TODO

    def test_list_staff(self):
        pass  # TODO

    def test_list_tutoring_groups(self):
        pass  # TODO

    def test_list_meetings(self):
        pass  # TODO

    def test_list_past_meetings(self):
        pass  # TODO

    def test_list_next_meetings(self):
        pass  # TODO
