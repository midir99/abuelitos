import datetime

from django.db.models import Q
from django.views import generic as views_generic

from . import choices, forms, models


class HomeView(views_generic.TemplateView):
    template_name = "th_olian/base.html"


home_view = HomeView.as_view()


class PeopleSearchView(views_generic.ListView):
    template_name = "civilizations/people_search_form.html"
    model = models.Person
    paginate_by = 50

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
            context["options_for_agem_code"] = (
                models.Locality.objects.get_municipalities_of_state(agee_code)
            )
            agem_code = self.request.GET.get("agem_code")
            if agem_code:
                for m in context["options_for_agem_code"]:
                    m["is_selected"] = m["agem_code"] == agem_code
                context["options_for_loc_code"] = (
                    models.Locality.objects.get_localities_of_municipality(
                        agee_code, agem_code
                    )
                )
                loc_code = self.request.GET.get("loc_code")
                if loc_code:
                    for l in context["options_for_loc_code"]:
                        l["is_selected"] = l["loc_code"] == loc_code
        return context

    def get_queryset(self):
        queryset = models.Person.objects.all()
        form = forms.PeopleSearchForm(self.request.GET)
        if not form.is_valid():
            return queryset
        full_name_or_alias = form.cleaned_data["full_name_or_alias"]
        if full_name_or_alias:
            queryset = queryset.filter(
                Q(full_name__icontains=full_name_or_alias)
                | Q(alias__icontains=full_name_or_alias)
            )
        year_of_birth = form.cleaned_data["year_of_birth"]
        if year_of_birth is not None:
            date_start = (
                datetime.date(year_of_birth - 5, 1, 1)
                if year_of_birth >= 5
                else datetime.date(1, 1, 1)
            )
            date_end = datetime.date(year_of_birth + 5, 12, 31)
            queryset = queryset.filter(date_of_birth__range=(date_start, date_end))
        year_of_death = form.cleaned_data["year_of_death"]
        if year_of_death is not None:
            date_start = (
                datetime.date(year_of_death - 5, 1, 1)
                if year_of_death >= 5
                else datetime.date(1, 1, 1)
            )
            date_end = datetime.date(year_of_death + 5, 12, 31)
            queryset = queryset.filter(date_of_death__range=(date_start, date_end))
        agee_code = form.cleaned_data["agee_code"]
        if agee_code:
            queryset = queryset.filter(locality__agee_code=agee_code)
        agem_code = form.cleaned_data["agem_code"]
        if agem_code:
            queryset = queryset.filter(locality__agem_code=agem_code)
        loc_code = form.cleaned_data["loc_code"]
        if loc_code:
            queryset = queryset.filter(locality__loc_code=loc_code)
        return queryset


people_search_view = PeopleSearchView.as_view()


class OptionsForAGEMCodeView(views_generic.TemplateView):
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


class OptionsForLocCodeView(views_generic.TemplateView):
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
