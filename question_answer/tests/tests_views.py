from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory
from question_answer.models import Collection
from question_answer.serializers import CollectionSerializer
from question_answer.tests.base_question_answer_test import BaseQuestionAnswerTestCase
from question_answer.views import CollectionViewSet
from faker import Faker


class CollectionsViewSetTest(BaseQuestionAnswerTestCase):

    def setUp(self):
        super().setUp()

    def test_get_all_card_groups_for_user(self):
        """
        Ensure we only return to the user's collections
        """
        factory = APIRequestFactory()
        user = self.user_1
        view = CollectionViewSet.as_view({'get': 'list'})

        # Get the collections via API request
        request = factory.get('/api/card-groups/')
        force_authenticate(request, user=user)
        response = view(request)

        # Get the collections and filter by user
        collections = Collection.objects.filter(user=user)
        serializer = CollectionSerializer(collections, many=True)

        # Check we get the same collections from both the request and by manager
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        not_user_1_list = []
        for entry in response.data:
            if entry["user"] != user.id:
                not_user_1_list.append(entry["user"])

        # If the list doesn't contain any users then all collections belong to user
        self.assertListEqual(not_user_1_list, [])

    def tearDown(self) -> None:
        super().tearDown()
