from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CardGroup, Card
from .serializers import CardSerializer, CardGroupSerializer, CardlessGroupSerializer


# Create your views here.


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardGroupViewSet(viewsets.ModelViewSet):
    queryset = CardGroup.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        print(self.action)
        if self.action in ("create", "update", "partial_update"):
            return CardlessGroupSerializer
        return CardGroupSerializer
