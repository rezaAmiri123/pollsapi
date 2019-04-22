from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from polls import views
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        # API Client will adding
        self.client = APIClient()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email='test@example.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri,
                HTTP_AUTHORIZATION=f'Token {self.token.key}')
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, '
                         f'received {response.status_code} instead.')

    def test_list2(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, '
                         f'received {response.status_code} instead.')

    def test_create(self):
        self.client.login(username='test', password='test')
        params = {
            'question': "How are you today?",
            'created_by': 1
        }
        response = self.client.post(self.uri, data=params)
        self.assertEqual(response.status_code, 201,
                 'Expected Response Code 201, received {0} instead.'
                 .format(response.status_code))
