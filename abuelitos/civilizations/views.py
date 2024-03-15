from django.views import generic as generic_views

from .forms import PeopleSearchForm


class HomeView(generic_views.TemplateView):
    template_name = "th_olian/base.html"


home_view = HomeView.as_view()


class PeopleSearchView(generic_views.TemplateView):
    template_name = "civilizations/people_search_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PeopleSearchForm(self.request.GET)
        return context


people_search_view = PeopleSearchView.as_view()

