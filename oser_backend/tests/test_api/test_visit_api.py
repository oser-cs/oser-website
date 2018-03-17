"""Visit API tests."""

from django.test import TestCase
from rest_framework import status

from tests.utils import HyperlinkedAPITestCase, SerializerTestCaseMixin
from visits.factory import VisitFactory
from visits.serializers import VisitSerializer


class VisitEndpointsTest(HyperlinkedAPITestCase):
    """Test access to the visits endpoints."""

    factory = VisitFactory
    serializer_class = VisitSerializer

    def perform_list(self):
        url = '/api/visits/'
        response = self.client.get(url)
        return response

    def test_list_authentication_required(self):
        self.assertRequiresAuth(
            self.perform_list, expected_status_code=status.HTTP_200_OK)

    def perform_retrieve(self):
        obj = self.factory.create()
        url = '/api/visits/{obj.pk}/'.format(obj=obj)
        response = self.client.get(url)
        return response

    def test_retrieve_authentication_required(self):
        self.assertRequiresAuth(
            self.perform_retrieve, expected_status_code=status.HTTP_200_OK)

    def perform_list_participants(self, obj=None):
        if obj is None:
            obj = self.factory.create()
        url = '/api/visits/{obj.pk}/participants/'.format(obj=obj)
        response = self.client.get(url)
        return response


class VisitSerializerTestCase(SerializerTestCaseMixin, TestCase):
    """Test the VisitSerializer."""

    serializer_class = VisitSerializer
    factory_class = VisitFactory

    expected_fields = (
        'id', 'url',
        'title', 'summary', 'description',
        'place', 'date', 'passed', 'deadline', 'registrations_open',
        'participants', 'organizers',
        'attached_files', 'image', 'fact_sheet',
    )