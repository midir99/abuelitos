from django.db import models
from django.db.models import functions


class LocalityManager(models.Manager):
    """Custom manager for Locality entities."""

    def get_municipalities_of_state(self, agee_code):
        return (
            self.get_queryset()
            .filter(agee_code=agee_code)
            .values("agee_code", "agee_name", "agem_code", "agem_name")
            .distinct()
        )

    def get_localities_of_municipality(self, agee_code, agem_code):
        return (
            self.get_queryset()
            .filter(agee_code=agee_code, agem_code=agem_code)
            .values(
                "agee_code",
                "agee_name",
                "agem_code",
                "agem_name",
                "loc_code",
                "loc_name",
            )
            .distinct()
        )
