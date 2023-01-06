from django.urls import include, path
from rest_framework import routers, urls
from . import views


router = routers.DefaultRouter()
router.register('api/questions', views.QuestionViewSet)
router.register('api/collections', views.CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(urls)),
]
