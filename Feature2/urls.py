from django.urls import path
from views import suggest_titles_view
urlpatterns = [
    path("suggest-titles/", suggest_titles_view),
]

