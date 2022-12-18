from django.db import models


class CardGroup(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='card_groups')

    def __str__(self):
        return self.title


class Card(models.Model):
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
    group = models.ForeignKey(
        CardGroup,
        on_delete=models.CASCADE,
        related_name='cards',
    )

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.title




