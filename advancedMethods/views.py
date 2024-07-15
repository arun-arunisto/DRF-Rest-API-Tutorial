from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import *
from .models import LoginCredUsers, FileUpload
import logging
from rest_framework.viewsets import generics
from rest_framework.views import APIView
import hashlib
from .program_utils import ProgramUtils
from .decorators import require_authentication, require_authentication_cls, require_admin_authentication
import os
from django.http import FileResponse
from urllib.parse import unquote
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from rest_framework.authentication import BaseAuthentication, get_authorization_header




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

    #mail sending using django
    def post(self, request):
        serialized_data = LogCredSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            #print(serialized_data.data["mail_id"])
            send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com", [serialized_data.data["mail_id"]])
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

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

#uploading a file
@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serialized_data = FileUploadSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UploadFileClassView(generics.GenericAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def download_file(request):
    if request.method == "GET":
        #sanitizing the filename
        filename = "git-cheat-sheet-education.pdf"
        filename = os.path.basename(unquote(filename))
        file_path = os.path.join("/home/royalbrothers/work/APITutorial/DRF-Rest-API-Tutorial/media/uploads", filename)
        print(os.path.exists(file_path))
        if os.path.exists(file_path):
            try:
                response = FileResponse(open(file_path, 'rb'))
                response['Content-Disposition'] = f"attachment, filename='{filename}'"
                return response
            except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"something went wrong"}, status=status.HTTP_404_NOT_FOUND)
        
class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        return super().get_queryset().order_by("-id")

class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return super().get_queryset().order_by("-id")

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class AdminUsersListCreateAPIView(generics.ListCreateAPIView):
    queryset = AdminUsers.objects.all()
    serializer_class = AdminUsersSerializer
    
    def get_queryset(self):
        return super().get_queryset().order_by("-id")

class AdminUsersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminUsers.objects.all()
    serializer_class = AdminUsersSerializer

class OrdersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return super().get_queryset().order_by("-id")

class OrdersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class AdminLoginFormViewSet(generics.GenericAPIView):
    serializer_class = AdminLoginFormSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            username = serialized_data.validated_data["username"]
            password = serialized_data.validated_data["password"]
            try:
                admin_data = AdminUsers.objects.get(name=username)
            except AdminUsers.DoesNotExist:
                return Response({"message":"Invalid username/password"})
            if admin_data.password == hashlib.sha256(password.encode()).hexdigest():
                data = AdminUsers.objects.select_related("location_id").filter(name=username).values("id", "location_id__id")
                # print(data[0])
                request.session["location_id"] = data[0]["location_id__id"]
                request.session["admin_id"] = data[0]["id"]
                return Response({"location_id":request.session["location_id"],
                                 "admin_id":request.session["admin_id"]}, status=status.HTTP_200_OK)
                # return Response({"data":data})
            else:
                return Response({"message":"Invalid username/password"})
        else:
            return Response({"message":"Something went wrong!!"})



@method_decorator(require_admin_authentication, name="dispatch")
class LocationListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs.get("location").id)
        data = Location.objects.get(id=1)
        serialized_data = LocationSerializer(data)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serialized_data = LocationSerializer(data=serialized_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response({"error":"Something went wrong when we create a data"}, status=status.HTTP_400_BAD_REQUEST)


#trying to use decorator for a specific method
@method_decorator(require_admin_authentication, name="post")
class LocationListAPIViewMethodDecoratorSpecific(APIView):
    def get(self, request, *args, **kwargs):
        data = Location.objects.all()
        serialized_data = LocationSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serialized_data = LocationSerializer(data=serialized_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response({"error":"Something went wrong when we create a data"}, status=status.HTTP_400_BAD_REQUEST)

#for celery and redis
class PremiumUsersListCreateAPIView(generics.ListCreateAPIView):
    queryset  = PremiumUsers.objects.all()
    serializer_class = PremiumUsersSerializer

class PremiumSubscriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = PremiumSubscription.objects.all()
    serializer_class = PremiumSubscriptionSerializer