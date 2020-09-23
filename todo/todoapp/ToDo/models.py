from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=1000)
    completed = models.BooleanField()





    """
    steps to create table in sqllite and share it with admin pannel.
    step1. we have to open models.py file and we write our code in this file by the help of models.py file our table can connect withadmins pannel
    step2.--->for creta table we have to create class in manage.py file with table name.
    step3-->and we have to run these two command to connect our database with django.
        1.-->python manage.py makemigration
        2.--->python manage.py migrate
        3.--> python manage.py createsuperuser
      step--> Register your app in setting.py file.  
    step4--> we can create varibles in models.py file according to our feilds in tables.
    step5---> import models(Database) file into admin file.
    step6---> register your table for admin... 
    """