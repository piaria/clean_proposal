from django.http import JsonResponse, Http404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.api.serializers.user_detail_serializer import UserDetailSerializer
from user.adapter.logic.dtos import UserData
from user.adapter.logic.exceptions import DomainModelNotFound
from user.adapter.logic.units_of_work import get_users, get_user_by_id, create_user, get_full_name
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

    @action(detail=False)
    def get_user_name(self, pk):
        return Response(
            get_full_name(pk)
        )
