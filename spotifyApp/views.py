from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Tracks
from .serializer import TrackSerializer

# Create your views here.
class TracksListView(APIView):
    def get(self, request):
        data = Tracks.objects.all()
        serialized_data = TrackSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = TrackSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackDetailView(APIView):
    def get(self, request, pk):
        data = Tracks.objects.get(id=pk)
        serialized_data = TrackSerializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data  = Tracks.objects.get(id=pk)
        serialized_data = TrackSerializer(data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = Tracks.objects.get(id=pk)
        data.delete()
        return Response({"message":"Deleted Successfully!!"})




