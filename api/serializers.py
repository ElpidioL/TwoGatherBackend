from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = str(user.id)
        token['name'] = user.name
        token['email'] = user.email
        token['phone'] = user.phone
        token['photo'] = user.photo
        token['description'] = user.description
        token['status'] = user.status
        token['lastActive'] = user.lastActive
        token['role'] = user.idRole.name if user.idRole else ''
        token['isAdmin'] = user.isAdmin
        token['pke'] = user.pke
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = str(self.user.id)
        data['name'] = self.user.name
        data['email'] = self.user.email
        data['phone'] = self.user.phone
        data['photo'] = self.user.photo
        data['description'] = self.user.description
        data['status'] = self.user.status
        data['lastActive'] = self.user.lastActive
        data['role'] = self.user.idRole.name if self.user.idRole else ''
        data['isAdmin'] = self.user.isAdmin
        data['pke'] = self.user.pke
        return data