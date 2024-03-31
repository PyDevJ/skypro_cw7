from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView, HabitAllAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('', HabitAllAPIView.as_view(), name='habit-all'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit-delete'),
]
