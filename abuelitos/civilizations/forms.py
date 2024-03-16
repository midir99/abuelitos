from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from . import choices


class PeopleSearchForm(forms.Form):
    full_name = forms.CharField(
        required=False,
        max_length=200,
        min_length=1,
    )
    year_of_birth = forms.IntegerField(
        required=False,
        min_value=0,
    )
    year_of_death = forms.IntegerField(
        required=False,
        min_value=0,
    )
    agee_code = forms.ChoiceField(
        required=False,
        choices=choices.AGEECode.choices,
    )
    agem_code = forms.CharField(
        required=False,
        max_length=3,
    )
    loc_code = forms.CharField(
        required=False,
        max_length=4,
    )

    def clean(self):
        cleaned_data = super().clean()
        year_of_birth = cleaned_data.get("year_of_birth")
        year_of_death = cleaned_data.get("year_of_death")
        if year_of_birth and year_of_death:
            if year_of_birth > year_of_death:
                self.add_error(
                    "year_of_death",
                    _("The year of death cannot be earlier than the year of birth."),
                )
        return cleaned_data
