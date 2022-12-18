from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user_management.views import UserTokenObtainPairView
from user_management import views

urlpatterns = [
    path('', views.getRoutes),
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
