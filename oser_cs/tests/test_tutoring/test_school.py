"""School model tests."""

from django.contrib.auth import get_user_model
import tutoring.models
from tests.utils import ModelTestCase
from tests.factory import SchoolFactory

User = get_user_model()


class SchoolTest(ModelTestCase):
    """Test the School model."""

    model = tutoring.models.School
    field_tests = {
        'uai_code': {
            'unique': True,
            'primary_key': True,
            'max_length': 8,
            'verbose_name': 'code UAI',
        },
        'name': {
            'verbose_name': 'nom',
        },
        'address': {
            'verbose_name': 'adresse',
        }
    }
    # TODO implement
    model_tests = {
        'verbose_name': 'lycée',
        'ordering': ('name',),
    }

    @classmethod
    def setUpTestData(cls):
        cls.obj = SchoolFactory.create(name='Lycée Michelin')

    def test_uai_code_help_text_indicates_format(self):
        help_text = self.model._meta.get_field('uai_code').help_text
        self.assertIsNotNone(help_text)
        self.assertIn('UAI', help_text)
        self.assertIn('ex-RNE', help_text)
        self.assertIn('7 chiffres', help_text)
        self.assertIn('une lettre', help_text)

    def test_uai_code_help_text_indicates_where_to_find_it(self):
        help_text = self.model._meta.get_field('uai_code').help_text
        self.assertIn("site du ministère de l'Éducation Nationale", help_text)

    def test_get_absolute_url(self):
        url = self.obj.get_absolute_url()
        self.assertEqual(url, f'/api/schools/{self.obj.uai_code}/')
        response = self.client.get(f'/api/schools/{self.obj.uai_code}/')
        self.assertEqual(200, response.status_code)
