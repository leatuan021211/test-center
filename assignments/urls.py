from django.urls import path
from .views import AssignmentListView, AssignmentRetrieveView, AssignmentSubmissionCreateView

urlpatterns = [
    path('', AssignmentListView.as_view(), name='assignment-list'),
    path('<int:pk>/', AssignmentRetrieveView.as_view(), name='assignment-detail'),
    path('<int:pk>/questions', AssignmentRetrieveView.as_view(), name='assignment-questions'),
    path('submission/', AssignmentSubmissionCreateView.as_view(), name='assignment-submission'),
    
]