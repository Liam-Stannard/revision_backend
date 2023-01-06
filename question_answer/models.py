from django.db import models


class Collection(models.Model):
    """
    A collection of questions which belong to a user
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='collections')

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    A question which belongs to a user and a collection
    """
    ANSWER_A = 0
    ANSWER_B = 1
    ANSWER_C = 2
    ANSWER_D = 3

    ANSWER_CHOICES = [
        (ANSWER_A, 'A'),
        (ANSWER_B, 'B'),
        (ANSWER_C, 'C'),
        (ANSWER_D, 'D'),
    ]

    title = models.CharField(max_length=50)
    question = models.CharField(max_length=250)
    correct_answer = models.IntegerField(
        choices=ANSWER_CHOICES,
        default=ANSWER_A)
    answer_a = models.CharField(max_length=250)
    answer_b = models.CharField(max_length=250)
    answer_c = models.CharField(max_length=250)
    answer_d = models.CharField(max_length=250)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='questions',
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.title




