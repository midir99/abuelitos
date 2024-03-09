import uuid

from django.contrib.auth import models as auth_models
from django.db import models
from django.urls import reverse_lazy


class User(auth_models.AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return reverse_lazy("accounts:profile")
