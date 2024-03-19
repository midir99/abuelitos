import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from . import choices


class PeopleSearchForm(forms.Form):
    full_name_or_alias = forms.CharField(
        required=False,
        max_length=200,
        min_length=1,
    )
    year_of_birth = forms.IntegerField(
        required=False,
        min_value=1,
    )
    year_of_death = forms.IntegerField(
        required=False,
        min_value=1,
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

    def clean_year_of_birth(self):
        year_of_birth = self.cleaned_data["year_of_birth"]
        if year_of_birth is None:
            return year_of_birth
        tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
        current_year = datetime.datetime.now(tz=tzinfo).year
        if year_of_birth > current_year:
            raise ValidationError(_("The year of birth cannot be later than %(current_year)s." % {"current_year": current_year}))
        return year_of_birth

    def clean_year_of_death(self):
        year_of_death = self.cleaned_data["year_of_death"]
        if year_of_death is None:
            return year_of_death
        tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
        current_year = datetime.datetime.now(tz=tzinfo).year
        if year_of_death > current_year:
            raise ValidationError(_("The year of death cannot be later than %(current_year)s." % {"current_year": current_year}))
        return year_of_death

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
