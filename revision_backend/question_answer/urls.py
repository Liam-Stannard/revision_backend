from django.urls import include, path
from rest_framework import routers, urls
from . import views


router = routers.DefaultRouter()
router.register('api/cards', views.CardViewSet)
router.register('api/groups', views.CardGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(urls)),


]
