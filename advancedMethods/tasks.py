#for testing the cron jobs
#adding a simple task for testing
#task 1: Printing Hello world in every one minute
#task 2: Sending a mail in every hour
from datetime import datetime
from django.core.mail import send_mail

#task 1
def printing_hello_world_in_every_min():
    print("Hello World", datetime.now())

#task 2
def send_mail_in_every_one_hr():
    send_mail("TEST MAIL", "test mail for django", "arun.a@royalbrothers.com",["arun.arunisto2@gmail.com"])


#for printing on terminal you need to call the function
printing_hello_world_in_every_min()