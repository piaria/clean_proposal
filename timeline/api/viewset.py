from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from timeline.api.serializers import EntryDetailSerializer

from user.api.serializers import UserDetailSerializer
from ..business_logic.exceptions import DomainModelNotFound
from ..business_logic.units_of_work import get_timeline


class TimelineViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving the timeline.
    """

    def list(self, request):
        timeline = get_timeline()
        serializer = EntryDetailSerializer(timeline, many=True)
        return Response(serializer.data)
