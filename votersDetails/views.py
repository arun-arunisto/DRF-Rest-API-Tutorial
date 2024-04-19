from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Voters
from .serializer import VotersSerializer

# Create your views here.
class VotersListView(APIView):
    def get(self, request):
        data = Voters.objects.all()
        serialized_data = VotersSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    def post(self, request):
        serialized_data = VotersSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class VotersDetailView(APIView):
    def get(self, request, pk):
        data = Voters.objects.get(id=pk)
        serialized_data = VotersSerializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = Voters.objects.get(id=pk)
        serialized_data = VotersSerializer(data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = Voters.objects.get(id=pk)
        data.delete()
        return Response({"Message":"Deleted Successfully!!"})
