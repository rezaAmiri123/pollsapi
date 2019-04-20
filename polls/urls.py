from django.urls import path
from .views import polls_list, polls_detail, PollList, PollDetail

app_name = 'polls'

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_detail"),

    path("polls/", PollList.as_view(), name='poll_list'),
    path("polls/<int:pk>/", PollDetail.as_view(), name='poll_detail'),
]
