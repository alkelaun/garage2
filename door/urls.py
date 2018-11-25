from django.urls import path
from .views import DoorClass, ViewClass, TestProxyView


urlpatterns = [

    path('', DoorClass.as_view()),
    path('v/<path>/', TestProxyView.as_view()),
]
