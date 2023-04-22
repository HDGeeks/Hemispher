from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *

class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SurveyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer 


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()

class QuestionAnswerViewSet(ModelViewSet):
    serializer_class = QuestionAnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = QuestionAnswer.objects.all()