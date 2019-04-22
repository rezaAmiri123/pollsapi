from django.urls import path
from .views import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from .views import PollViewSet
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'polls'

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api_login/', obtain_auth_token, name="api_login"),
    path("polls/", PollList.as_view(), name='poll_list'),
    path("polls/<int:pk>/", PollDetail.as_view(), name='poll_detail'),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name='choice_list'),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name='user_create'),
]

urlpatterns += router.urls
