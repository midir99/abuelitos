from django.urls import path

from . import views

app_name = "civilizations"

urlpatterns = [
    path("", views.people_search_view, name="people_search"),
    path(
        "options_for_agem_code/",
        views.options_for_agem_code_view,
        name="options_for_agem_code",
    ),
    path(
        "options_for_loc_code/",
        views.options_for_loc_code_view,
        name="options_for_loc_code",
    ),
]
