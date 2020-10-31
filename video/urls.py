from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('view/<int:video_id>/', views.view, name='view'),
]