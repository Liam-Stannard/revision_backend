from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Extension of super class TokenObtainPairSerializer to allow the contents of the
    token to be customised
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
