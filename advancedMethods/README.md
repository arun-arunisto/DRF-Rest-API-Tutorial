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



