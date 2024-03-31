from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание новой привычки."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек пользователя."""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitAllAPIView(generics.ListAPIView):
    """Просмотр всех публичных привычек."""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.all().filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаление привычки."""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
