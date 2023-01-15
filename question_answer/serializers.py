from rest_framework import serializers
from .function import json_deserialize
from .models import Question, Collection


class QuestionSerializer(serializers.ModelSerializer):
    """
     A serializer for questions
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), )

    class Meta:
        model = Question
        fields = ('id', 'title', 'question', 'correct_answer', 'collection',
                  'answer_a', 'answer_b', 'answer_c', 'answer_d', 'user')


class CollectionSerializer(serializers.ModelSerializer):
    """
    A serializer for collections which includes cards in the post
    """
    questions = QuestionSerializer(read_only=True, many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), )

    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'user', 'questions']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        print("In create")
        question_data = validated_data.pop('cards')
        collection = Collection.objects.create(**validated_data)
        for question_data in question_data:
            Question.objects.create(group=collection, **question_data)
        return collection

    def update(self, instance, validated_data):
        request = self.context['request']
        question_data = request.data.get('cards')
        cards_ids = json_deserialize(question_data, expect_type=list)
        validated_data['cards'] = cards_ids
        instance = super().update(instance, validated_data)
        return instance


class QuestionlessCollectionSerializer(serializers.ModelSerializer):
    """
    A serializer for collections which does not include cards in the post.
    This allows for collections to be created without cards
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), )

    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        collection = Collection.objects.create(**validated_data)
        return collection
