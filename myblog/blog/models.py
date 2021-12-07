from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from twilio.rest import Client
from ckeditor.fields import RichTextField

# Create your models here.

class Author(models.Model):
    name = models.TextField(max_length=100, default='namesssss')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class comments(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class tempUser(models.Model):
    tempname = models.CharField(max_length=50)
    number = models.IntegerField()
    emailid = models.EmailField(max_length=80)
    qwertypass = models.CharField(max_length=20)
    unique = models.TextField(primary_key=True, help_text='Unique ID for this person')

    def __str__(self):
        return str(self.number)
    def save(self, *args, **kwargs):
        account_sid = "ACCOUNT_SID"
        auth_token = 'AUTH_TOKEN'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=f'This is your OTP for {self.tempname} : {self.unique}',
                                    from_='+PhoneNumber', #enter_number_from_which_you_want_to_send_message
                                    to=f'+91{self.number}'
                                )
        print(message.sid)


        return super().save(*args, **kwargs)
