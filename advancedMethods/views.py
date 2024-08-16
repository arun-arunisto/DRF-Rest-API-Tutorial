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
from django.db.models import F,  Value, Prefetch
from django.db.models.functions import Concat
from .helpers import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser



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

class BikeListCreateView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

class BikeModelListCreateView(generics.ListCreateAPIView):
    queryset = BikeModel.objects.all()
    serializer_class = BikeModelSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class IndexView(APIView):
    def get(self, request):
        data = Booking.objects.all().values("start_date", "end_date", booking_id=F("id"), register_no=F("bike__register_no"), model_name=F("bike__model__name"))
        serialized_data = IndexViewSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

class BlockReviewListCreateView(generics.ListCreateAPIView):
    queryset = BlockReview.objects.all()
    serializer_class = BlockReviewSerializer

class RidesListCreateView(generics.ListCreateAPIView):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer

class IndexViewUpdateView(APIView):
    def get(self, request):
        data = Rides.objects.select_related("bike", "booking").prefetch_related("booking__blockreview_set").filter(
            booking__blockreview__block_status=0).values(
                "start_date", "end_date",
                register_no=F("bike__register_no"),
                block_reason=F("booking__blockreview__block_reason"),
                block_status=F("booking__blockreview__block_status"),
            )
        serialized_data = IndexViewUpdateSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

#bulk image upload
class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def post(self, request, *args, **kwargs):
        bike_id = request.data.get("bike")

        if not bike_id:
            return Response({"message": "Bike ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        #converting querydict to original dict
        images = request.FILES.getlist("image")

        if not images:
            return Response({"message": "Image is required"}, status=status.HTTP_400_BAD_REQUEST)

        for img_name in images:
            modified_data = modify_input_for_multiple_files(bike_id, img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
            else:
                return Response({"message":file_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"successfully uploaded"}, status=status.HTTP_201_CREATED)
"""
class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        property_id = request.data['property_id']

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(property_id,
                                                            img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)
"""
"""
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from .models import Images

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def post(self, request, *args, **kwargs):
        bike_id = request.data.get("bike")

        if not bike_id:
            return Response({"message": "Bike ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Converting querydict to original dict
        images = request.FILES.getlist('image')
        if not images:
            return Response({"message": "No images found"}, status=status.HTTP_400_BAD_REQUEST)

        for img in images:
            modified_data = modify_input_for_multiple_files(bike_id, img)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Successfully uploaded"}, status=status.HTTP_201_CREATED)

def modify_input_for_multiple_files(bike_id, image):
    return {
        'bike': bike_id,
        'image': image
    }

"""

class TripListCreateView(APIView):
    def get(self, request):
        data = Trip.objects.all().values("id", "bike", "start_time", "end_time", "description", "status")
        serialized_data = TripSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serialized_data = TripSerializerPost(data=request.data)
        if serialized_data.is_valid():
            bike = serialized_data.validated_data["bike"]
            start_time = serialized_data.validated_data["start_time"]
            end_time = serialized_data.validated_data["end_time"]
            description = serialized_data.validated_data["description"]
            trip_status = serialized_data.validated_data["status"]
            images = request.FILES.getlist("images")
            bike_data = Bike.objects.get(id=bike)
            trip_data = Trip.objects.create(bike=bike_data, start_time=start_time, end_time=end_time, description=description, status=trip_status)
            if images:
                for img in images:
                    img_data = multiple_image_adding_function(img)
                    TripImages.objects.create(trip=trip_data, filename=img_data["image_name"], image_data=img_data["binary_image"])
            return Response({"message":"Trip created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class TripDetailView(APIView):
    def get(self, request, id):
        trip_queryset = Trip.objects.filter(id=id).values("id", "bike", "start_time", "end_time", "description", "status")
        trip = trip_queryset.first()
        serialized_data = TripSerializerDetailView(trip)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class UserRoleCreateView(APIView):
    def get(self, request):
        data = UserRoles.objects.all().values("role_name", "permissions")
        serialized_data = userRoleSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = userRoleSerializer(data=request.data)
        if serialized_data.is_valid():
            UserRoles.objects.create(**serialized_data.validated_data)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)