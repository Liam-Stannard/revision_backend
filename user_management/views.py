from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from user_management.serializers import UserTokenObtainPairSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    """
    Extension of super TokenObtainPairView to allow for custom UserTokenObtainPairSerializer to be used
    """
    serializer_class = UserTokenObtainPairSerializer


def getRoutes(request):
    """
    Static function to return possible routes
    :param request: The request
    :return: Possible routes a JSON response
    """
    routes = [
        'token',
        'token/refresh'
    ]
    return JsonResponse(routes, safe=False)
