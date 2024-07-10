#for testing the cron jobs
#adding a simple task for testing
#task 1: Sending a mail in every hour
from django.core.mail import send_mail


#task 1
def send_mail_in_every_one_hr():
    send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com",["arun.arunisto2@gmail.com"])
