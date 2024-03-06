from django.views import generic as generic_views


class HomeView(generic_views.TemplateView):
    template_name = "th_olian/base.html"


home_view = HomeView.as_view()
