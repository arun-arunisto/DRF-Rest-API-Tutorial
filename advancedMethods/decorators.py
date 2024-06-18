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


