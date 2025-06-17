from django.urls import path
import views


urlpatterns = [
    path('transcribe/', views.transcribe_audio, name='transcribe'),
]