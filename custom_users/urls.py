from django.urls import path
from .views import UserInformationRetrieveUpdateView

urlpatterns = [
    path("profile/", UserInformationRetrieveUpdateView.as_view(), name="user-information-retrieve-update"),
]
