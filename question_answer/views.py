from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Collection, Card
from .permissions import IsOwner
from .serializers import CardSerializer, CollectionSerializer, CardlessCollectionSerializer


# Create your views here.


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filtered_queryset = self.queryset.filter(owner=self.request.user)
        return filtered_queryset


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filtered_queryset = self.queryset.filter(owner=self.request.user)
        return filtered_queryset

    def get_serializer_class(self):
        print(self.action)
        if self.action in ("create", "update", "partial_update"):
            return CardlessCollectionSerializer
        return CollectionSerializer
