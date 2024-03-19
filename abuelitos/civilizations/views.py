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
        context["options_for_agee_code"] = []
        context["options_for_agem_code"] = []
        context["options_for_loc_code"] = []
        agee_code = self.request.GET.get("agee_code")
        if agee_code in choices.AGEECode:
            context["options_for_agee_code"] = [
                {
                    "agee_code": state.value,
                    "agee_name": state.label,
                    "is_selected": state.value == agee_code,
                }
                for state in choices.AGEECode
            ]
            agem_code = self.request.GET.get("agem_code")
            if agem_code:
                context["options_for_agem_code"] = (
                    models.Locality.objects.get_municipalities_of_state(agee_code)
                )
                for m in context["options_for_agem_code"]:
                    m["is_selected"] = m["agem_code"] == agem_code
                loc_code = self.request.GET.get("loc_code")
                if loc_code:
                    context["options_for_loc_code"] = (
                        models.Locality.objects.get_localities_of_municipality(
                            agee_code, agem_code
                        )
                    )
                    for l in context["options_for_loc_code"]:
                        l["is_selected"] = l["loc_code"] == loc_code

        return context


people_search_view = PeopleSearchView.as_view()


class OptionsForAGEMCodeView(generic_views.TemplateView):
    template_name = "civilizations/options_for_agem_code.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agee_code = self.request.GET.get("agee_code")
        context["localities"] = []
        if agee_code in choices.AGEECode:
            context["localities"] = models.Locality.objects.get_municipalities_of_state(
                agee_code
            )
        return context


options_for_agem_code_view = OptionsForAGEMCodeView.as_view()


class OptionsForLocCodeView(generic_views.TemplateView):
    template_name = "civilizations/options_for_loc_code.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agee_code = self.request.GET.get("agee_code")
        agem_code = self.request.GET.get("agem_code")
        context["localities"] = models.Locality.objects.get_localities_of_municipality(
            agee_code, agem_code
        )
        return context


options_for_loc_code_view = OptionsForLocCodeView.as_view()
