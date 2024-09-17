from django.db import router
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitsListAPIView,
    HabitsCreateAPIView,
    HabitsRetrieveAPIView,
    HabitsUpdateAPIView,
    HabitsDestroyAPIView,
    HabitsPublicListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="habits_list"),
    path("create/", HabitsCreateAPIView.as_view(), name="habits_create"),
    path("<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habits_retrieve"),
    path(
        "<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits_update"
    ),
    path(
        "<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits_delete"
    ),
    path("public/", HabitsPublicListAPIView.as_view(), name="public"),
]

