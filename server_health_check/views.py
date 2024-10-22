from rest_framework.response import Response
from rest_framework.views import APIView
import sentry_sdk


# Create your views here.
class HealthCheckView(APIView):
    def get(self, request):
        data = {
            "status":"OK",
            "Database":self.check_database(),
            "Server":self.check_server()
        }
        return Response(data)
    
    def check_database(self):
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
            connection.close()
            if result == (1,):
                return "Database is working fine!"
            else:
                return "Database connection failed!"
        except Exception as e:
            return "Checking connection db is failed:"+str(e)
    
    def check_server(self):
        import psutil

        cpu_percent  =psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        return {
            "CPU Count":psutil.cpu_count(),
            "CPU Usage":"{:.1f}%".format(cpu_percent),
            "Memory Usage":"{:.1f}%".format(memory.percent),
            "Disk Usage":"{:.1f}%".format(disk.percent),
            "Current Running Processes Count":len(list(psutil.pids())),
            "Running Processes": list(set([proc.name() for proc in psutil.process_iter()]))
        }

#for checking the sentry debug mode
class TestAPIView(APIView):
    def get(self, request):
        try:
            result = 1/0
            return Response({"result":result})
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)