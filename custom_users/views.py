from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView
from .models import CustomUser
from .serializers import UserInformationSerializer

class UserInformationRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInformationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
