from django.urls import path
from .views import WeekCounterView

urlpatterns = [
    path('week/', WeekCounterView.as_view(), name='week')
]
