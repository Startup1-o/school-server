from django.urls import path

from register_school.api.v1.views import TeamDetailsView, TeamsView


urlpatterns = [
    path("<int:team_id>/", TeamDetailsView.as_view(), name="team_details"),
    path("", TeamsView.as_view(), name="teams"),
]

app_name = "teams"
