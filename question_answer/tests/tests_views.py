from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from question_answer.models import CardGroup
from question_answer.serializers import CardGroupSerializer
from question_answer.views import CardGroupViewSet


class CardGroupViewSetTest(TestCase):

    def setUp(self):
        owner_1_username = 'owner_1'
        owner_1_password = '12345'

        owner_2_username = 'owner_2'
        owner_2_password = '54321'

        owner_1 = User.objects.create_user(username=owner_1_username)
        owner_1.set_password(owner_1_password)
        owner_1.save()

        owner_2 = User.objects.create_user(username=owner_2_username)
        owner_2.set_password(owner_2_password)
        owner_2.save()

        CardGroup.objects.create(title='Python Django Revision',
                                 description='Python Django revision questions.',
                                 owner=owner_1)

        CardGroup.objects.create(title='Python Revision',
                                 description='Python revision questions.',
                                 owner=owner_2)
        CardGroup.objects.create(title='AZ-900 Revision',
                                 description='AZ-900 revision questions.',
                                 owner=owner_2)

    def test_get_all_card_groups_for_user(self):

        factory = APIRequestFactory()
        user = User.objects.get(username='owner_1')
        view = CardGroupViewSet.as_view({'get': 'list'})

        request = factory.get('/api/card-groups/')
        force_authenticate(request, user=user)
        response = view(request)

        card_groups = CardGroup.objects.filter(owner=user)
        serializer = CardGroupSerializer(card_groups, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
