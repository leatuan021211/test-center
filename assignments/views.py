from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Assignment, AssignmentQuestion
from .serializers import AssignmentSerializer, AssignmentQuestionSerializer, AssignmentSubmissionSerializer

class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Assignment.objects.filter(assignee=user)
    

class AssignmentRetrieveView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Assignment.objects.filter(assignee=user)
    
    
class AssignmentQuestionListView(generics.ListAPIView):
    queryset = AssignmentQuestion.objects.all()
    serializer_class = AssignmentQuestionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return AssignmentQuestion.objects.filter(assignment__assignee=user, assignment__id=self.kwargs.get('pk'))
    

class AssignmentSubmissionCreateView(generics.CreateAPIView):
    serializer_class = AssignmentSubmissionSerializer
    permission_classes = [IsAuthenticated]