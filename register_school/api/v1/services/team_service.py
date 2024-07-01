from register_school.api.v1.serializers import TeamsSerializer
from register_school.models import Teams
from rest_framework import status


class BaseService(object):
    def __init__(self):
        self.response = {"code": "", "data": {}, "errors": {}, "message": ""}

    @property
    def ret(self):
        return self.response

    def set_response(self, code=status.HTTP_200_OK, data={}, errors={}, message="Success"):
        self.response = {
            "code": code,
            "data": data,
            "errors": errors,
            "message": message,
        }
        return self.response

    def set_data(self, data):
        self.response["data"] = data
        return self.response

    def set_errors(self, errors):
        self.response["errors"] = errors
        return self.response

    def set_message(self, message):
        self.message = message

    # ----------  2XX response code ----------

    @classmethod
    def get_200_response(cls, data, message="Success"):
        return {
            "code": status.HTTP_200_OK,
            "data": data,
            "errors": {},
            "message": message,
        }

    @classmethod
    def get_201_response(cls, data, message="Created Successfully"):
        return {
            "code": status.HTTP_201_CREATED,
            "data": data,
            "errors": {},
            "message": message,
        }

    @classmethod
    def get_204_response(cls):
        return status.HTTP_204_NO_CONTENT

    # ----------  4XX response code ----------

    @classmethod
    def get_400_response(cls, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_400_BAD_REQUEST,
            "data": data,
            "errors": errors,
            "message": message,
        }

    def get_baked_400_response(self, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_400_BAD_REQUEST,
            "data": data,
            "errors": errors,
            "message": message,
        }

    @classmethod
    def get_401_response(cls, errors, data={}, message="Unauthorized Request"):
        return {
            "code": status.HTTP_401_UNAUTHORIZED,
            "data": data,
            "errors": errors,
            "message": message,
        }

    def get_baked_401_response(self, errors, data={}, message="Unauthorized Request"):
        return {
            "code": status.HTTP_401_UNAUTHORIZED,
            "data": data,
            "errors": errors,
            "message": message,
        }

    @classmethod
    def get_403_response(cls, errors, data={}, message="Forbidden"):
        return {
            "code": status.HTTP_403_FORBIDDEN,
            "data": data,
            "errors": errors,
            "message": message,
        }

    def get_baked_403_response(self, errors, data={}, message="Forbidden"):
        return {
            "code": status.HTTP_403_FORBIDDEN,
            "data": data,
            "errors": errors,
            "message": message,
        }

    @classmethod
    def get_404_response(cls, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_404_NOT_FOUND,
            "data": data,
            "errors": errors,
            "message": message,
        }

    def get_baked_404_response(self, errors, data={}, message="Bad Request"):
        return {
            "code": status.HTTP_404_NOT_FOUND,
            "data": data,
            "errors": errors,
            "message": message,
        }

    @classmethod
    def get_412_response(cls, errors, data={}, message="Precondition Failed"):
        return {
            "code": status.HTTP_412_PRECONDITION_FAILED,
            "data": data,
            "errors": errors,
            "message": message,
        }

    def get_baked_412_response(self, errors, data={}, message="Precondition Failed"):
        return {
            "code": status.HTTP_412_PRECONDITION_FAILED,
            "data": data,
            "errors": errors,
            "message": message,
        }

    # ----------  5XX response code here ----------

    @classmethod
    def get_500_response(cls, data, errors={}, message="Internal Server Error"):
        return {
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "data": data,
            "errors": errors,
            "message": message,
        }


class TeamService(BaseService):
    def __init__(self, customer, team: Teams = None):
        self.customer = customer  # login_customer
        self.team = team

    def create_team(self, payload_data):
        create_data = TeamsSerializer(data=payload_data, context={"customer": self.owner})
        if create_data.is_valid():
            team = Teams.objects.create(**create_data.validated_data)
            return self.get_201_response(TeamsSerializer(team).data)
        return self.get_baked_400_response(create_data.errors)

    def get_user_teams(self, *args, **kwargs):
        teams_list = Teams.objects.all()
        teams_list = TeamsSerializer(teams_list, many=True)
        return self.get_200_response(data=teams_list.data)

    def get_team_details(self):
        serialized_data = TeamsSerializer(self.team).data
        return self.get_200_response(serialized_data)

    def update_team_details(self, request_data, *args, **kwargs):
        update_data = TeamsSerializer(self.team, data=request_data)
        if update_data.is_valid():
            team_obj_updated = update_data.save()
            serialized_data = TeamsSerializer(team_obj_updated).data
            return self.get_200_response(serialized_data)
        return self.get_baked_400_response(update_data.errors)

    def delete_team(self, *args, **kwargs):
        self.team.delete()
        return self.get_200_response({})
