from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataPoint
from .serializers import DataPointSerializer


class DataPointList(APIView):
    def get(self, request, format=None):
        datapoints = DataPoint.objects.all()
        serializer = DataPointSerializer(datapoints, many=True)
        return Response(serializer.data)
