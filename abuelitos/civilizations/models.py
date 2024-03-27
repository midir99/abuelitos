import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from . import managers


class Locality(models.Model):
    """
    The fields in this model were taken from the
    "Single Catalog of Keys of State, Municipal and Local Geostatistical Areas" report
    provided by the INEGI.

    https://www.inegi.org.mx/app/ageeml/

    In this project, Mexico is considered to be divided in states, municipalities
    and localities.

    The attributes agee_code and agee_name refer to the state.
    The attributes agem_code and agem_name refer to the municipalities.
    The attributes loc_code and loc_name refer to the localities.

    Here is an example of how to identify the locality of
    San Andres de la Cal, Tepoztlan, Morelos.

    State
    -----
    agee_code: 17
    agee_name: Morelos

    Municipality
    ------------
    agem_code: 020
    agem_name: Tepoztlan

    Locality
    --------
    loc_code: 0005
    loc_name: San Andres de la Cal
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    agee_code = models.CharField(
        _("AGEE code"),
        max_length=2,
        help_text=_("AGEE code of this locality."),
    )
    agee_name = models.CharField(
        _("AGEE name"),
        max_length=30,
        help_text=_("AGEE name of this locality."),
    )
    agem_code = models.CharField(
        _("AGEM code"),
        max_length=3,
        help_text=_("AGEM code of this locality."),
    )
    agem_name = models.CharField(
        _("AGEM name"),
        max_length=50,
        help_text=_("AGEM name of this locality."),
    )
    loc_code = models.CharField(
        _("locality code"),
        max_length=4,
        help_text=_("Code of this locality."),
    )
    loc_name = models.CharField(
        _("locality name"),
        max_length=50,
        help_text=_("Name of this locality."),
    )
    history = models.TextField(
        _("history"), blank=True, help_text=_("History of this locality.")
    )
    interesting_facts = models.TextField(
        _("interesting facts"),
        blank=True,
        help_text=_("Interesting facts about this locality."),
    )
    see_more_at = models.TextField(
        _("see more at"),
        blank=True,
        help_text=_(
            "Links or places where people can find more information about this locality."
        ),
    )
    picture_1 = models.ImageField(
        _("first picture"),
        upload_to="pictures/localities/",
        blank=True,
        help_text=_(
            "First picture of this locality that will be shown in its gallery."
        ),
    )
    picture_1_caption = models.CharField(
        _("first picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the first picture of this locality."),
    )
    picture_2 = models.ImageField(
        _("second picture"),
        upload_to="pictures/localities/",
        blank=True,
        help_text=_(
            "Second picture of this locality that will be shown in its gallery."
        ),
    )
    picture_2_caption = models.CharField(
        _("second picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the second picture of this locality."),
    )
    picture_3 = models.ImageField(
        _("third picture"),
        upload_to="pictures/localities/",
        blank=True,
        help_text=_(
            "Third picture of this locality that will be shown in its gallery."
        ),
    )
    picture_3_caption = models.CharField(
        _("third picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the third picture of this locality."),
    )
    picture_4 = models.ImageField(
        _("forth picture"),
        upload_to="pictures/localities/",
        blank=True,
        help_text=_(
            "Forth picture of this locality that will be shown in its gallery."
        ),
    )
    picture_4_caption = models.CharField(
        _("forth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the forth picture of this locality."),
    )
    picture_5 = models.ImageField(
        _("fifth picture"),
        upload_to="pictures/localities/",
        blank=True,
        help_text=_(
            "Fifth picture of this locality that will be shown in its gallery."
        ),
    )
    picture_5_caption = models.CharField(
        _("fifth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the fifth picture of this locality."),
    )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        max_length=50,
        help_text=_("Slug to identify this locality in the website."),
    )
    metadata = models.JSONField(
        _("metadata"),
        blank=True,
        default=dict,
        help_text=_(
            "Metadata for this record. Change it only if you know what you are doing!"
        ),
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_(
            "This timestamp shows when this record was created. This field is "
            "populated automatically."
        ),
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_(
            "This timestamp shows when this record was last updated. This field is "
            "populated automatically."
        ),
    )

    objects = managers.LocalityManager()

    class Meta:
        verbose_name = _("Locality")
        verbose_name_plural = _("Localities")
        constraints = [
            models.UniqueConstraint(
                name="unique_locality",
                fields=["agee_code", "agem_code", "loc_code"],
            )
        ]

    def __str__(self):
        return f"{self.loc_name}, {self.agem_name}, {self.agee_name}"


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    full_name = models.CharField(
        _("full name"),
        max_length=200,
        help_text=_("Full name of this person."),
    )
    alias = models.CharField(
        _("alias"),
        max_length=50,
        blank=True,
        help_text=_("Alias of this person."),
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        blank=True,
        null=True,
        help_text=_("Date of birth of this person."),
    )
    date_of_death = models.DateField(
        _("date of death"),
        blank=True,
        null=True,
        help_text=_("Date of death of this person."),
    )
    biography = models.TextField(
        _("biography"), blank=True, help_text=_("Biography of this person.")
    )
    autobiography = models.TextField(
        _("autobiography"),
        blank=True,
        help_text=_("Autobiography of this person."),
    )
    interesting_facts = models.TextField(
        _("interesting facts"),
        blank=True,
        help_text=_("Interesting facts about this person."),
    )
    anecdotes = models.TextField(
        _("anecdotes"),
        blank=True,
        help_text=_("Anecdotes of this person."),
    )
    see_more_at = models.TextField(
        _("see more at"),
        blank=True,
        help_text=_(
            "Links or places where people can find more information about this person."
        ),
    )
    picture_ft = models.ImageField(
        _("family tree picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_("Picture of this person that will be shown in the family tree."),
    )
    picture_1 = models.ImageField(
        _("first picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_(
            "First picture of this person that will be shown in their gallery."
        ),
    )
    picture_1_caption = models.CharField(
        _("first picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the first picture of this person."),
    )
    picture_2 = models.ImageField(
        _("second picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_(
            "Second picture of this person that will be shown in their gallery."
        ),
    )
    picture_2_caption = models.CharField(
        _("second picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the second picture of this person."),
    )
    picture_3 = models.ImageField(
        _("third picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_(
            "Third picture of this person that will be shown in their gallery."
        ),
    )
    picture_3_caption = models.CharField(
        _("third picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the third picture of this person."),
    )
    picture_4 = models.ImageField(
        _("forth picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_(
            "Forth picture of this person that will be shown in their gallery."
        ),
    )
    picture_4_caption = models.CharField(
        _("forth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the forth picture of this person."),
    )
    picture_5 = models.ImageField(
        _("fifth picture"),
        upload_to="pictures/people/",
        blank=True,
        help_text=_(
            "Fifth picture of this person that will be shown in their gallery."
        ),
    )
    picture_5_caption = models.CharField(
        _("fifth picture caption"),
        max_length=100,
        blank=True,
        help_text=_("Caption for the fifth picture of this person."),
    )
    father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="father+",
        blank=True,
        null=True,
        help_text=_("Father of this person."),
    )
    mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="mother+",
        blank=True,
        null=True,
        help_text=_("Mother of this person."),
    )
    locality = models.ForeignKey(
        Locality,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("Locality where this person lived most of their life."),
    )
    is_archived = models.BooleanField(
        _("is archived?"),
        default=False,
        help_text=_(
            "If archived, the website will show no information about this person."
        ),
    )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        max_length=50,
        help_text=_("Slug to identify this person in the website."),
    )
    metadata = models.JSONField(
        _("metadata"),
        blank=True,
        default=dict,
        help_text=_(
            "Metadata for this record. Change it only if you know what you are doing!"
        ),
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_(
            "This timestamp shows when this record was created. This field is "
            "populated automatically."
        ),
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_(
            "This timestamp shows when this record was last updated. This field is "
            "populated automatically."
        ),
    )

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    def get_absolute_url(self):
        return reverse("civilizations:person_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.full_name}"
