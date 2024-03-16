from django.urls import path

from . import views

app_name = "civilizations"

urlpatterns = [
    path("", views.people_search_view, name="people_search"),
    path(
        "options_for_municipalities/",
        views.options_for_municipalities_view,
        name="options_for_municipalities",
    ),
    path(
        "options_for_localities/",
        views.options_for_localities_view,
        name="options_for_localities",
    ),
]
