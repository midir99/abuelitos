from django.views import generic as generic_views

from . import choices, forms, models


class HomeView(generic_views.TemplateView):
    template_name = "th_olian/base.html"


home_view = HomeView.as_view()


class PeopleSearchView(generic_views.TemplateView):
    template_name = "civilizations/people_search_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.PeopleSearchForm(self.request.GET)
        return context


people_search_view = PeopleSearchView.as_view()


class OptionsForMunicipalitiesView(generic_views.TemplateView):
    template_name = "civilizations/options_for_municipalities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agee_code = self.request.GET.get("agee_code")
        context["municipalities"] = []
        if agee_code in choices.AGEECode:
            context["municipalities"] = (
                models.Locality.objects.get_municipalities_of_state(agee_code)
            )
        return context


options_for_municipalities_view = OptionsForMunicipalitiesView.as_view()


class OptionsForLocalitiesView(generic_views.TemplateView):
    template_name = "civilizations/options_for_localities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agee_code = self.request.GET.get("agee_code")
        agem_code = self.request.GET.get("agem_code")
        context["localities"] = models.Locality.objects.get_localities_of_municipality(
            agee_code, agem_code
        )
        return context


options_for_localities_view = OptionsForLocalitiesView.as_view()
