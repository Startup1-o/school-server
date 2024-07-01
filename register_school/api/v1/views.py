from register_school.api.v1.services.team_service import TeamService
from rest_framework.response import Response
from rest_framework.views import APIView

head_data = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "X-Requested-With, Content-Type, Set-Cookie",
    "content_type": "application/json",
}


class TeamsView(APIView):

    def post(self, request, *args, **kwargs):
        response = TeamService(request.customer, request.iam).create_team(request.data)
        return Response(response, status=response.get("code"), headers=head_data)

    def get(self, request, *args, **kwargs):
        response = TeamService(request.customer, request.iam).get_user_teams(**request.query_params.dict())
        return Response(response, status=response.get("code"), headers=head_data)


class TeamDetailsView(APIView):

    def get(self, request, *args, **kwargs):
        team = kwargs.get("team", None)
        response = TeamService(request.customer, request.iam, team).get_team_details()
        return Response(response, status=response.get("code"), headers=head_data)

    def put(self, request, *args, **kwargs):
        team = kwargs.get("team", None)
        response = TeamService(request.customer, request.iam, team).update_team_details(request.data, **kwargs)
        return Response(response, status=response.get("code"), headers=head_data)

    def delete(self, request, *args, **kwargs):
        team = kwargs.get("team", None)
        response = TeamService(request.customer, request.iam, team).delete_team(**kwargs)
        return Response(response, status=response.get("code"), headers=head_data)
