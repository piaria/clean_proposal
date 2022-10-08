from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MessageCreationSerializer, MessageDetailSerializer
from ..business_logic.exceptions import DomainModelNotFound
from ..business_logic.units_of_work import (
    create_message,
    get_message_by_id,
    get_messages,
)


class MessagesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving messages.
    """

    def list(self, request):

        return JsonResponse(
            [message.__dict__ for message in get_messages()], safe=False
        )

    def retrieve(self, request, pk=None):
        try:
            message = get_message_by_id(pk)
        except DomainModelNotFound:
            raise Http404()

        serializer = MessageDetailSerializer(message)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = create_message(**serializer.validated_data)
        return JsonResponse(message.__dict__, safe=False)
