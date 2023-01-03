# Generated by Django 4.1.3 on 2023-01-03 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=250)),
                ('correct_answer', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('answer_a', models.CharField(max_length=250)),
                ('answer_b', models.CharField(max_length=250)),
                ('answer_c', models.CharField(max_length=250)),
                ('answer_d', models.CharField(max_length=250)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='question_answer.collection')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
