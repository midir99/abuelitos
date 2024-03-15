from django.urls import path

from . import views

app_name = "civilizations"

urlpatterns = [
    path("", views.people_search_view, name="people_search"),
]
