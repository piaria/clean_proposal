from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from user.api.serializers import UserDetailSerializer
from user.business_logic.dtos import UserData
from ..business_logic.exceptions import DomainModelNotFound
from ..business_logic.units_of_work import get_users, get_user_by_id, create_user
from rest_typed.views import Body, typed_action


class UsersViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving messages.
    """

    def list(self, request):

        return JsonResponse([user.__dict__ for user in get_users()], safe=False)

    def retrieve(self, request, pk=None):
        try:
            user = get_user_by_id(pk)
        except DomainModelNotFound:
            raise Http404()

        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    @typed_action(detail=False, methods=["POST"])
    def post(self, user: UserData = Body()):
        user_created = create_user(
            first_name=user["first_name"], last_name=user["last_name"]
        )
        return Response(dict(user_created))
