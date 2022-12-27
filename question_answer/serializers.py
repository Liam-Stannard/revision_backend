from rest_framework import serializers
from .function import json_deserialize
from .models import Card, CardGroup


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ('id', 'title', 'question', 'correct_answer', 'group_id',
                  'answer_a', 'answer_b', 'answer_c', 'answer_d', 'owner')


class CardGroupSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = CardGroup
        fields = ['id', 'title', 'description', 'owner', 'cards']
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        print("In create")
        cards_data = validated_data.pop('cards')
        group = CardGroup.objects.create(**validated_data)
        for card_data in cards_data:
            Card.objects.create(group=group, **card_data)
        return group

    def update(self, instance, validated_data):
        request = self.context['request']
        cards_data = request.data.get('cards')
        cards_ids = json_deserialize(cards_data, expect_type=list)
        validated_data['cards'] = cards_ids
        instance = super().update(instance, validated_data)

        return instance


class CardlessGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardGroup
        fields = ['id', 'title', 'description', 'owner']

