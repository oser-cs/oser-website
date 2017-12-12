"""Tutoring API views."""

from rest_framework.viewsets import ModelViewSet

from tutoring.models import TutoringGroup, School, TutoringSession
from api.serializers.tutoring import (
    TutoringGroupSerializer,
    SchoolSerializer, SchoolCreateSerializer,
    TutoringSessionSerializer,
)

# Create your views here.


class TutoringGroupViewSet(ModelViewSet):
    """API endpoint that allows tutoring groups to be viewed or edited.

    Actions: list, retrieve, create, update, partial_update, destroy
    """

    queryset = TutoringGroup.objects.all()
    serializer_class = TutoringGroupSerializer

    def get_queryset(self):
        queryset = self.queryset
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class SchoolViewSet(ModelViewSet):
    """API endpoint that allows schools to be viewed, edited or destroyed.

    Actions: list, retrieve, create, update, partial_update, destroy
    """

    queryset = School.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return SchoolCreateSerializer
        return SchoolSerializer


class TutoringSessionViewSet(ModelViewSet):
    """API endpoint that allows tutoring sessions to be viewed or edited.

    Actions: list, retrieve, create, update, partial_update, destroy
    """

    queryset = TutoringSession.objects.all()
    serializer_class = TutoringSessionSerializer
