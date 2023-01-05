from django.contrib.auth.models import User
from django.test import TestCase
from question_answer.models import Collection
from faker import Faker


class BaseQuestionAnswerTestCase(TestCase):
    def setUp(self):
        """
        Create two unique users and some associated collections
        """

        faker = Faker()
        user_1_username = faker.user_name()
        user_1_password = faker.password()

        user_2_username = faker.user_name()
        user_2_password = faker.password()

        self.user_1 = User.objects.create_user(username=user_1_username)
        self.user_1.set_password(user_1_password)
        self.user_1.save()

        self.user_2 = User.objects.create_user(username=user_2_username)
        self.user_2.set_password(user_2_password)
        self.user_2.save()

        self.collections = []
        self.collections.append(Collection.objects.create(title=faker.sentence(nb_words=1),
                                                          description=faker.paragraph(nb_sentences=2),
                                                          user=self.user_1))

        self.collections.append(Collection.objects.create(title=faker.sentence(nb_words=1),
                                                          description=faker.paragraph(nb_sentences=2),
                                                          user=self.user_1))
        self.collections.append(Collection.objects.create(title=faker.sentence(nb_words=1),
                                                          description=faker.paragraph(nb_sentences=2),
                                                          user=self.user_2))

    def tearDown(self) -> None:
        self.user_1.delete()
        self.user_2.delete()
        for collection in self.collections:
            collection.delete()
