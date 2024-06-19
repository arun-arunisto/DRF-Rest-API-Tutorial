## 26.05.2024
So, we created the app and create two views now we are going to create our `CustomPermissions` for that first create a file on your app folder called `permission.py`, After that you need to import the necessary methods for the custom permissions so import it
```python
from rest_framework import permissions
```
Then create your permission class. Here i am going to create that only admin have the rights to edit/delete/create others have only to view that's our first permission `IsAdminUserOrReadOnly`. This is our class that i am going to create and the code i provided below
```python
from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
```
Here first we're importing the `permissions` from rest_framework then inherit from this to our class. Then we're return the True value for `SAFE_METHODS`. `SAFE_METHODS` are `GET`, `HEAD` and `OPTIONS` these are the safe methods remaining methods are the non safe methods. In else condition we checking that user is login and user have the is_staff access (it means admin access).
