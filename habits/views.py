from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginators import CustomPagination
from habits.serializer import HabitsSerializer
from users.permissions import IsOwner


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitsSerializer
    pagination_class = CustomPagination
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habits.objects.filter(user=user)


class HabitsPublicListAPIView(ListAPIView):
    serializer_class = HabitsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)


class HabitsCreateAPIView(CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitsRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsUpdateAPIView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
