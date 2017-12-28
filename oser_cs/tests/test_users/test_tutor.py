"""Tutor model tests."""

from tests.factory import TutorFactory
from tests.test_users.mixins import ProfileTestMixin
from tests.utils import ModelTestCase

from users.models import Tutor


class TutorTestCase(ProfileTestMixin, ModelTestCase):
    """Test case for Tutor model."""

    model = Tutor
    field_tests = {
        'promotion': {
            'blank': False,
        }
    }
    model_tests = {
        'verbose_name': 'tuteur',
    }

    @classmethod
    def setUpTestData(self):
        self.obj = TutorFactory.create()
