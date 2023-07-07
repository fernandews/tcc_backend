from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import LineString
from app.serializers import GeolocationSerializer
from rest_framework.response import Response
from http import HTTPStatus

class GeolocationView(APIView):
    def post(self, request):
        data = request.data.copy()
        linestring_data = data.pop('geolocation_data', None)
        
        if linestring_data is not None:
            linestring = LineString(linestring_data)
            data['geolocation_data'] = linestring

        serializer = GeolocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
