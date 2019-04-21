from .models import Poll, Vote, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializers, UserSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset

    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializers(data=data)
        if serializer.is_valid():
            vote = serializer.save().data
            return Response(data=vote, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

