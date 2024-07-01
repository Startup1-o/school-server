from django.db import models
from register_school.constants import TEAM_NAME_MAX_LENGTH


class Teams:
    name = models.CharField(max_length=TEAM_NAME_MAX_LENGTH)
    description = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return f"<Team({self.id}: {self.name}: {self.description})>"
