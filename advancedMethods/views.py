from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import *
from .models import LoginCredUsers
import logging
from rest_framework.viewsets import generics
from rest_framework.views import APIView
import hashlib
from .program_utils import ProgramUtils
from .decorators import require_authentication, require_authentication_cls


"""@api_view(['GET', 'POST'])
def advanced_methods(request):
    return Response({"message":"Hello World})"""

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
program_utils = ProgramUtils()

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == "POST":
        serialized_data = LogCredSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors)
    
    data = LoginCredUsers.objects.all().order_by("-id")
    serialized_data = LogCredSerializers(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_user(request, pk):
    try:
        user_data = LoginCredUsers.objects.get(id=pk)
    except LoginCredUsers.DoesNotExist:
        logger.error(f"User {pk} Doesn't exist!")
        return Response({"error":"User not found!"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serialized_data = LogCredSerializers(user_data, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        user_data.delete()
    if request.method == "GET":
        serialized_data = LogCredSerializers(user_data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


#class based views
class UserListView(generics.ListCreateAPIView):
    queryset = LoginCredUsers.objects.all()
    serializer_class = LogCredSerializers

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoginCredUsers.objects.all()
    serializer_class = LogCredSerializers

@api_view(["POST"])
def login_view(request):
    serialized_data = LoginFormSerializer(data=request.data)
    if serialized_data.is_valid():
        username = serialized_data.validated_data["username"]
        password = serialized_data.validated_data["pass_wd"]
        print(username, password)
        try:
            user_data = LoginCredUsers.objects.get(username=username)
        except LoginCredUsers.DoesNotExist:
            return Response({"error":"User not found!"}, status=status.HTTP_400_BAD_REQUEST)
        if user_data.pass_wd == hashlib.sha256(password.encode()).hexdigest():
            serialized_data = LogCredSerializers(user_data)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Username / Password is incorrect!"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serialized_data = LoginFormSerializer(data=request.data)
        if serialized_data.is_valid():
            username = serialized_data.validated_data["username"]
            password = serialized_data.validated_data["pass_wd"]

            try:
                user_data = LoginCredUsers.objects.get(username=username)
            except LoginCredUsers.DoesNotExist:
                return Response({"error":"User not found!"}, status=status.HTTP_404_NOT_FOUND)
            
            if user_data.pass_wd == hashlib.sha256(password.encode()).hexdigest():
                serialized_data = LogCredSerializers(user_data)
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            else:
                return Response({"error":"Username / Password is incorrect!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginFormSerializer

    def post(self, request):
        serialized_data = LoginFormSerializer(data=request.data)
        if serialized_data.is_valid():
            username = serialized_data.validated_data["username"]
            password = serialized_data.validated_data["pass_wd"]
            try:
                user_data = LoginCredUsers.objects.get(username=username)
            except LoginCredUsers.DoesNotExist:
                return Response({"error":"User not found"}, status=status.HTTP_404_NOT_FOUND)
            if user_data.pass_wd == hashlib.sha256(password.encode()).hexdigest():
                serialized_data = LogCredSerializers(user_data)
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            else:
                return Response({"error":"Username / Password Incorrect."})
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginNGenerate(generics.GenericAPIView):
    serializer_class = LoginFormSerializer

    def post(self, request):
        serialized_data = LoginFormSerializer(data=request.data)
        if serialized_data.is_valid():
            username = serialized_data.validated_data["username"]
            password = serialized_data.validated_data["pass_wd"]
            try:
                user_data = LoginCredUsers.objects.get(username=username)
            except LoginCredUsers.DoesNotExist:
                return Response({"message":"User not found."}, status=status.HTTP_404_NOT_FOUND)
            if user_data.pass_wd == hashlib.sha256(password.encode()).hexdigest():
                request.session["secret_key"] = program_utils.generate_secret_key()
                request.session["auth_status"] = True
                return Response({"secret_key":request.session["secret_key"]}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Username / Password incorrect."})
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def logout(request):
    request.session.clear()
    return Response({"message":"Logged out successfully"}, status=status.HTTP_200_OK)


@api_view()
@require_authentication
def hello_world(request):
    return Response({"message":"hello world"}, status=status.HTTP_200_OK)


class UserDetailViewAuth(generics.GenericAPIView):
    @require_authentication_cls
    def get(self, request, *args, **kwargs):
        user_data = LoginCredUsers.objects.get(id=kwargs['pk'])
        serialized_data = LogCredSerializers(user_data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
