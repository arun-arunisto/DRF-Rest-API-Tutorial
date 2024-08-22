## 18.06.2024
Added `logging` method to the application, this is mainly used to record the events like (errors, info's, warning) during the time of execution.

Then on `advancedMethod` application we're creating two functions for (`create_user`, `edit_user`) create and edit an user. And the `hashing` password method implemented on the `serializer` file. So, you dont need to write code at your `views` file it will automatically updates and saves your data in your database.

```Python
class LogCredSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginCredUsers
        fields = "__all__"

    #here we will implement the hashing password logic when the time of creating user   
    def create(self, validated_data):
        user = LoginCredUsers(**validated_data)
        user.hash_passwrd(validated_data['pass_wd'])
        user.save()
        return user

    #update method if there will be data present in the validated_data before updating the user
    def update(self, instance, validated_data):
        if 'pass_wd' in validated_data:
            instance.hash_passwrd(validated_data['pass_wd'])
            validated_data['pass_wd'] = instance.pass_wd
        return super().update(instance, validated_data)
```

Now we will see the above same functions how to execute on the `class-based` views (`UserListView` and `UserDetailView`).


### Login Form
Next we're going to add the login method using the above data. For that first we're going to create two form fields using `serializer` module like below

```Python
class LoginFormSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    pass_wd = serializers.CharField(write_only=True)
    class Meta:
        model = LoginCredUsers
        exclude = ("mail_id",)
```
above we created two fields to enter the data and on the meta class excluded the `mail_id` field because we only need the `username` and `password` for the login. And first we are executing this method on function-based view (`login_view`)

Next we're going to see how this operation work on class-based view `LoginView`. And then after that we will execute the same functionality on the class based viewset view `LoginViewSet`

### Decorators 
Our next topic is `decorators`, in thistopic we're going to implement our own decorator function called `require_authentication` for that first we're going to create an python file called `decorators.py`.

And i am going to create a simple decorator that will check if `session` have a `secret_key` and also value of `session` `auth_status` is `True`.

So, for that if the user login then a `secret_key` generate and it will stored on `session`. For creating a 32 len secret key i am going to use my function from `program_utils.py` file on my application. 

Then i am going to create a class based view called `LoginNGenerate`, this class is used to generate a secret_key after login. And our concept is this secret_key everytime change when login

And also i am creating a simple function for `logout`. When the time of user clicks the `logout` the session data will clear

Now it's time to write the decorator

```Python
from .models import LoginCredUsers
from rest_framework import status
from rest_framework.response import Response


def require_authentication(view_func):
    def wrapper(request):
        try:
            secret_key = request.session["secret_key"]
            auth_status = request.session["auth_status"]
        except:
            return Response({"message":"Login required"}, status=status.HTTP_400_BAD_REQUEST)
        if len(secret_key) == 0 or auth_status != True:
            return Response({"message":"Login required."}, status=status.HTTP_400_BAD_REQUEST)
        return view_func(request)
    return wrapper
```
The above code i provided for the `decorators`

So, we successfully executed the decorators on function based view (`hello-world`)

```Python
@api_view()
@require_authentication
def hello_world(request):
    return Response({"message":"hello world"}, status=status.HTTP_200_OK)
```
Next we need to implement decorators on class based views.

## 19.06.2024
### File Upload
Today we are going to implement the uploading files in our rest_framework.
To upload file using restframework we need to follow some steps

First we need to create a model to file. Here first we're going to use `FileField`. 

```Python
class FileUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
```
After adding a model dont forget to make migrate.

After making these changes, we're going to add this on serializers. like below,

```Python
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"
```
First we're going to implement this on a function based view like below
```Python
@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serialized_data = FileUploadSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
```
After adding the view route to the url in `urls.py` file. Then configure the media settings in your `settings.py` file, like below,
```Python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
``` 
And configure the media files on your `urls.py` file in your application folder like below.

```Python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

You can test the endpoint using the below command

```bash
curl -X -F "file=@<path-to-your-file>" http://127.0.0.1:8000/<endpoint>/
```
Now we're going to look how this works on class-based views

```Python
class UploadFileClassView(generics.GenericAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.error, status=status.HTTP_400_BAD_REQUEST)
```
### File Download
Next, we are going to look into how to enable the option for users to download the file. First we are going to create a Function based view, like below.

```Python

```

## 24.06.2024 
### Sending an Email
Today configuring and sending emails using Django's mail method first we need to configure our EMAIL in our settings.py file, like below,

```Python
#settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
```

Then import the send_mail() method from django like below

```Python
from django.core.mail import send_mail
```
Then you can simply send mail using this method like below 

```Python
send_mail("<subject>", "<message>", "<from_mail_id>", "<to_mail_id>")
```

## 10.07.2024
To configure `django-crontab` on your project, first add the package in `INSTALLED_APPS` at your `settings.py`, like below:
```Python
#settings.py
INSTALLED_APPS = [
    django_crontab,
]
```
After adding the module create a file named `tasks.py` on your application folder, then add yoour cron tasks there. Here, i am simply create a task for sending email every one hour. For, that task you dont want to import anything from `django-crontab` you can simply add a task like a normal function like below

```Python
# tasks.py
#for testing the cron jobs
#adding a simple task for testing
#task 1: Sending a mail in every hour
from django.core.mail import send_mail


#task 1
def send_mail_in_every_one_hr():
    send_mail("TEST MAIL", "test mail for django", "<from_mail_id>",["<to_mail_id>"])

```

After adding the task you need to configure your `CRON_JOBS` on your application, for that open your `settings.py` and configure `CRONJOBS` like below:

```Python
#settings.py
#configuring cron jobs to the application
CRONJOBS = [
    #adding the task for every hour
    ('0 * * * *', 'advancedMethods.tasks.send_mail_in_every_one_hr'),

]
```
`'0 * * * *'` - This is the `cron expression` for set the timings so, here i am sending mail in every one hour. This `'0 * * * *'` expression represents the timing every 1 hour.

After configuring the `CRONJOBS` to add all `CRONJOBS` to `cron tab`, use the below command

```bash
python manage.py crontab add
```
To show the current active jobs in your project, use the below command

```bash
python manage.py crontab show
```

To remove the jobs from your `cron tab` use the below command

```bash
python manage.py crontab remove
```
Then, do this ...
You can also generate your own `cron expressions`, there's lots of free available websites are there to generate `cron expresions`.


## 12.07.2024
 Today going to learn how to set a cron job using `celery` module and backend cache server as `redis`, first we installed the required packages using the commands on main directory `README.md` after that need to include it in `INSTALLED_APPS` on  `settings.py` file, like below:

 ```Python
 #settings.py
 INSTALLED_APPS = [
    'celery',
    'django_celery_results',
    'django_celery_beat',
    'django_redis',
 ]
 ```

 After adding it on `INSTALLED_APPS` file need to configure the redis server on `settings.py` file, like below:

```Python
# REDIS CACHE
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
} 
```
After configuring the `REDIS` to project, going to configure `celery` on project like below:

```Python
#celery settings
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_TIMEZONE = 'Asia/Kolkata'

```
Now the `celery` and `redis` configured successfully, next need to create an application for celery for that create a file named `celery.py` on the project folder then configure with your project like below:

```Python
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<project_folder_name>.settings')

app = Celery('<project_folder_name>')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')



app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
```
> [!NOTE]
> on the <project_folder_name> give your project name


After creating `celery.py` file initialize the celery app to your project for that open the `__init__.py` file on the project folder and add the below code to your project.

```Python
#project_folder/__init__.py
from .celery import app as celery_app


__all__ = ("celery_app",)
```

For the `celery`, `redis` concepts going to create new two tables on my `models.py` one is `PremiumUsers` and other one is `PremiumSubscription` so, we're going to create users and going to set their premium subscription start and end date and their premium status is going to be `True` and we're going to schedule a task in `celery` that whenever the end date comes the celery will do the background job that set `False` for their premium status and the table look like below:

```Python
#models.py
#for celery and redis
class PremiumUsers(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    mail_id = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    premium_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Premium user: {self.name}"

class PremiumSubscription(models.Model):
    user = models.ForeignKey(PremiumUsers, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Premium subscription: {self.user.name}"
```
next we're going to migrate it. using our `makemigrations` and `migrate` script. Then going to create serializers for two models that created above.

```Python
#serializer.py
class PremiumUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumUsers
        fields = "__all__"

class PremiumSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumSubscription
        fields = "__all__"
```
After that going to create views.

```Python
#views.py
#for celery and redis
class PremiumUsersListCreateAPIView(generics.ListCreateAPIView):
    queryset  = PremiumUsers.objects.all()
    serializer_class = PremiumUsersSerializer

class PremiumSubscriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = PremiumSubscription.objects.all()
    serializer_class = PremiumSubscriptionSerializer
```
Created views for the models that we are going to use.

> [!NOTE]
> I didn't mention the url routeing on `urls.py` for this two views so please find the url_routeing on `urls.py` file.


Next our logic is whenever any user add to `PremiumSubscription` our `celery` going to schedule task with their premium subscription end time for that first we need to create a Task. For that create a file on your `app directory` and name it as `tasks.py`, and add the task that you want to schedule like below:

```Python
#tasks.py
#import the required modules for celery
from celery import shared_task
from .models import PremiumSubscription, PremiumUsers
from datetime import datetime


@shared_task
def subscription_terminate_worker(id): #worker
    try:
        end_time = PremiumSubscription.objects.filter(user__id=id, user__premium_status=True).order_by("-id").first().end_date
        time_count = (end_time - datetime.now()).total_seconds()
        if time_count > 0:
            print("Task is added to queue")
            subscription_termination.apply_async(args=[id], countdown=time_count)
            print("Task scheduled successfully")
    except PremiumSubscription.DoesNotExist:
        print("Data does not exist")
    except Exception as e:
        print(e)


@shared_task
def subscription_termination(id): #job
    premium_user = PremiumUsers.objects.get(id=id)
    premium_user.premium_status = False
    premium_user.save()
    print("Task executed successfully")
```

After creating the task execute the task where want to, in this tutorial I am going to use it on my serializers where i am adding my data:

```Python
#serializer.py
class PremiumSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumSubscription
        fields = "__all__"

    def create(self, validated_data):
        premium = PremiumSubscription(**validated_data)
        premium_user = PremiumUsers.objects.get(id=premium.user.id)
        premium_user.premium_status = True
        premium_user.save()
        premium.save()
        subscription_terminate_worker.delay(premium_user.id) #scheduled task
        return premium
```

After all the step use the below code to start the `redis-server` on a terminal and don't forget to activate your virtual environment,

```CommandPrompt
redis-server --port 6380 --replicaof 127.0.0.1 6379
```

Then start your django server:

```CommandPrompt
python manage.py runserver
```

After that open a new terminal on the same directory where you running your django project and run the below sxcript to start the `celery-worker`:

```CommandPrompt
celery -A <your_project_name> worker -l info
```
Then open new terminal on the same dir.

```CommandPrompt
celery -A <your_project_name> beat -l info
```

Then open a new terminal on the same dir for `flower`

```CommandPrompt
celery -A <your_project_folder> flower -l info
```

> [!NOTE]
> Don't forget to activate your python virtual environment on every terminal

> [!IMPORTANT]
> for accessing flower use port 5555 [http:127.0.0.1:5555](http://127.0.0.1:5555/)

And you can monitor the redis-server using command line tool `redis-cli` or with `redisinsight`

Next we're going to look into how to execute `corn jobs` using `celery`. corn jobs also we're going to write a new task that sending an mail daily at 09.00AM

for that first we're going to create a task first then execute it in the cron jobs, so open your `tasks.py` and create a new task like below:

```Python
#for cron jobs
@shared_task
def send_email_celery():
    send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com",["arun.arunisto2@gmail.com"])
```

After that open your `settings.py` file on your project folder and schedule the corn job at `09:00AM` everyday using `CELERY_BEAT_SCHEDULER`, before that you need to import a module `crontab` from `celery.scheduler`

```Python
from celery.scheduler import crontab

CELERY_BEAT_SCHEDULE = {
    'recurring-task': {
        'task': '<app_name>.tasks.<task_name>',
        'schedule': crontab(hour=09, minute=00)
    },
}
```
## 15.07.2024
One Serializer for multiple columns in mulitple table

For this create a serializer using `serializers.Serializer` class and then add fields like below:

```Python
class IndexViewSerializer(serializers.Serializer):
    booking_id = serializers.CharField(max_length=100)
    register_no = serializers.CharField(max_length=100)
    model_name = serializers.CharField(max_length=100)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
```

After that you can annotate the data from your model (if there any case the fields name differ in serializer like below) to annotate you can use `F` from  `django.db.models` 

```Python
class IndexView(APIView):
    def get(self, request):
        data = Booking.objects.all().values("start_date", "end_date", booking_id=F("id"), register_no=F("bike__register_no"), model_name=F("bike__model__name"))
        serialized_data = IndexViewSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
```

## 16.07.2024
Accessing elements from multiple tables like the scenario below:

```Python
#models.py
class Bike(models.Model):
    register_no = models.CharField(max_length=100, blank=False, null=False, unique=True)
    model = models.ForeignKey(BikeModel, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Register No: {self.register_no}"

class Booking(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking: {self.bike.register_no}"

class BlockReview(models.Model):
    block_reason = models.IntegerField(choices=((1, "Service"), (2, "brake down"), (3, "puncture")), null=False, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, blank=False)
    block_status = models.IntegerField(choices=((0, "Pending"), (1, "rejected"), (2, "accepted")), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Block review: {self.block_reason}"

class Rides(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride: {self.bike.register_no}"
```

From the below example using ORM query and fetching data's using `Rides` table, the query look like below:

```Python
#ORM query
from django.db.models import F, Value
from django.db.models.functions import Concat

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
```

- Bulk image uploading, for that first i create a model named `Image` to save the data like below

```Python
class Images(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to="uploads/")
```

Then serializer like below:

```Python
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
```

Then added a `helpers.py` file and added the below code:

```Python
def modify_input_for_multiple_files(bike, image):
    return {
        'bike': bike,
        'image': image
    }

```

Then views like below,

```Python
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
```

The above method we used to upload multiple images at one time.

## 13.08.2024
For the `SerializerMethodField` created new models to demonstrate the the above topics:

```Python
class Trip(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip: {self.id}"
    
class TripImages(models.Model):
    path = models.CharField(max_length=500, blank=True, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=False, blank=False)
    image_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip image: {self.id}"
```

Next we're going to add serializer and views for above models.

```Python
#serializer.py

class TripSerializerPost(serializers.Serializer):
    bike = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.IntegerField()

class TripImageSerializer(serializers.Serializer):
    path = serializers.CharField()
    trip = serializers.IntegerField()
    image_data = Base64BinaryField()

#Trip serializer with serializer method field
class TripSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bike = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return status_choices.get(obj["status"], "Unknown Status")
    

class TripSerializerDetailView(serializers.Serializer):
    id = serializers.IntegerField()
    bike = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    description = serializers.CharField()
    status = serializers.SerializerMethodField()
    block_images = serializers.SerializerMethodField()

    def get_status(self, obj):
        return status_choices.get(obj["status"], "Unknown Status")

    def get_block_images(self, obj):
        images = TripImages.objects.filter(trip__id=obj["id"])
        if images:
            return [image.filename for image in images]
        else:
            return []

#views.py

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
```

On the above example we are obtaining the values from `TripImages` table and added into list then passing the data through serializer to the API using `SeializerMethodField`, and also on my current projct I am using `SerializerMethodField` for the options like above shown `status` 

## 16.08.2024

Adding JSON data to database for that created table with `JSONField()` column like below

```Python
#models.py
class UserRoles(models.Model):
    role_name = models.CharField(unique=True, blank=False, null=False, max_length=100)
    permissions = models.JSONField()

    def __str__(self):
        return self.role_name
```

And serializer also

```Python
class userRoleSerializer(serializers.Serializer):
    role_name = serializers.CharField()
    permissions = serializers.JSONField()
```
Then views:

```Python
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
```

## 22.08.2024

Working on `perform-create` method of generic views, to perform the `perform_create` created new two tables on models

```Python
class TestTable1(models.Model):
    col_1 = models.CharField(unique=True, blank=False, null=False, max_length=100)
    col_2 = models.CharField(blank=False, null=False, max_length=100)
    col_3 = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return f"Test Table 1 Data: {self.id}"

class TestTable2(models.Model):
    test_table = models.ForeignKey(TestTable1, on_delete=models.CASCADE, null=False, blank=False)
    col_1 = models.CharField(unique=True, blank=False, null=False, max_length=100)
    col_2 = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return f"Test Table 2 Data: {self.id}"
```

And going to perfom the operation that whenever trying to save data on `TestTable1` using `generics` views simultaneously going to update the `TestTable2` for that we're going to use `perform_create` method.