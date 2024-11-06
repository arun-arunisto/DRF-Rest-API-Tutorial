from rest_framework import status
from rest_framework.response import Response
from .models import *
# from django.utils.decorators import method_decorator
from functools import wraps



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



def require_authentication_cls(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            secret_key = request.session["secret_key"]
            auth_status = request.session["auth_status"]
        except:
            return Response({"message":"Login required"}, status=status.HTTP_400_BAD_REQUEST)
        if len(secret_key) == 0 or auth_status != True:
            return Response({"message":"Login required."}, status=status.HTTP_400_BAD_REQUEST)
        return view_func(request, *args, **kwargs)
    return wrapper

def require_admin_authentication(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_status = False
        try:
            location_id = 1 #request.META.get("LOCATION_ID")
            admin_id = 1 #request.META.get("ADMIN_ID")
            if location_id and admin_id:
                auth_status = True 
        except:
            auth_status = False
            kwargs.update({"auth_status":auth_status})
            return view_func(request, *args, **kwargs)
        if auth_status:
            try:
                location_data = Location.objects.get(id=location_id)
                products_data = Products.objects.filter(location_id=location_data)
            except Exception as e:
                print(e)
            # try:
            #     #location_data = Location.objects.get(id=location_id)
            #     #products = Products.objects.select_related("location_id").filter(location_id=location_data.id)
            #     #products = Products.objects.select_related("loaction_id").filter(location_id__id=location.id)
            # except Location.DoesNotExist:
            #     return Response({"message":"Something went wrong on fetching location"}, status=status.HTTP_400_BAD_REQUEST)
            # except Products.DoesNotExist:
            #     return Response({"message":"Something went wrong on fetching products"}, status=status.HTTP_400_BAD_REQUEST)
            # except Exception as e:
            #     return Response({"message":e}, status=status.HTTP_400_BAD_REQUEST)
            #updating kwargs with data that we need to pass
            #kwargs.update({"location":location_data, "products":products, "admin_id":admin_id, "auth_status":auth_status})
            kwargs.update({"location":location_data, "products":products_data})
            print(kwargs)
            return view_func(request, *args, **kwargs)
        kwargs.update({"auth_status":auth_status})
        return view_func(request, *args, **kwargs)
    return wrapper


# def apply_decorator(view_cls):
#     @method_decorator(require_admin_authentication, name="dispatch")
#     class Wrapper(view_cls):
#         def dispatch(self, request, *args, **kwargs):
#             if not kwargs.get("admin_id"):
#                 return Response({"message":"Login required."}, status=status.HTTP_400_BAD_REQUEST)
#             return super(Wrapper, self).dispatch(request, *args, **kwargs)
#     return Wrapper
