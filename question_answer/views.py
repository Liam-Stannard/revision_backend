from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Collection, Question
from .permissions import IsOwner
from .serializers import QuestionSerializer, CollectionSerializer, QuestionlessCollectionSerializer


# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Only return query results which belong to the user
        """
        filtered_queryset = self.queryset.filter(user=self.request.user)
        return filtered_queryset


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Only return query results which belong to the user
        """
        filtered_queryset = self.queryset.filter(user=self.request.user)
        return filtered_queryset

    def get_serializer_class(self):
        """
        If creating or updating the collection use a questionless serializer as we wouldn't
        questions to be updated via this mechanism else serialize the collection in full
        """
        print(self.action)
        if self.action in ("create", "update", "partial_update"):
            return QuestionlessCollectionSerializer
        return CollectionSerializer
