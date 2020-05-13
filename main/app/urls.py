
from . import views
from django.urls import path, include

urlpatterns = [
    path('api/app/', views.ModeloneListCreate.as_view() ),
]
