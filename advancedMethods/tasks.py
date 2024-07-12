#for testing the cron jobs
#adding a simple task for testing
#task 1: Sending a mail in every hour
from django.core.mail import send_mail
#import the required modules for celery
from celery import shared_task
from .models import PremiumSubscription, PremiumUsers
from datetime import datetime


#task 1
def send_mail_in_every_one_hr(id):
    send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com",["arun.arunisto2@gmail.com"])


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



#for cron jobs
@shared_task
def send_email_celery():
    send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com",["arun.arunisto2@gmail.com"])