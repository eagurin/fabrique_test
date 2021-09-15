from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import VoteFilter
from .models import Poll, Question, Vote
from .permissions import PollPermission, QuestionPermission
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (PollPermission,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission,)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ("get", "post")
    filterset_class = VoteFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)

        return super().perform_create(serializer)
