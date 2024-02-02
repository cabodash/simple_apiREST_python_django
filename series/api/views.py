from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from series.api.serializers import ModelSerieSerializer
from series.models import Serie


class SerieApiView(ViewSet):

    def list(self, request):
        series = ModelSerieSerializer(Serie.objects.all(), many=True)
        return Response(data=series.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: int):
        series = ModelSerieSerializer(Serie.objects.get(pk=pk))
        return Response(data=series.data, status=status.HTTP_200_OK)

    def create(self, request):
        serie = ModelSerieSerializer(data=request.POST)
        serie.is_valid(raise_exception=True)
        Serie.objects.create(title=serie.validated_data['title'], description=serie.validated_data['description'])
        return self.list(request)
