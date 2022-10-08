from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from user.api.serializers import UserDetailSerializer
from ..business_logic.exceptions import DomainModelNotFound
from ..business_logic.units_of_work import (
    get_users,
    get_user_by_id,
    create_user
)


class UsersViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving messages.
    """

    def list(self, request):

        return JsonResponse(
            [user.__dict__ for user in get_users()], safe=False
        )

    def retrieve(self, request, pk=None):
        try:
            user = get_user_by_id(pk)
        except DomainModelNotFound:
            raise Http404()

        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = create_user(**serializer.validated_data)
        return JsonResponse(message.__dict__, safe=False)
