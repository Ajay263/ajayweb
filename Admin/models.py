from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Contact_form1(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.



# About

class About(models.Model):
    birthday = models.DateField()
    degree_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Email = models.EmailField()
    website = models.URLField()
    age = models.IntegerField()
    occupation = models.CharField(max_length=120)
    freelancer = models.CharField(max_length=20)
    Description_top = models.TextField()
    Description_bottom = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/')

# ListView for Portfolio items
class Portfolio(models.Model):
    Category = models.CharField(max_length=80)
    Client = models.CharField(max_length=50)
    Project_date = models.DateTimeField()
    Project_Details = models.TextField()
    Project_URL = models.CharField(max_length=80)
    image1 = models.ImageField(null=True,blank=True,upload_to='images/')
    image2 = models.ImageField(null=True, blank=True,upload_to='images/')
    image3 = models.ImageField(null=True, blank=True,upload_to='images/')
    icon_image = models.ImageField(null=True, blank=True,upload_to='images/')
    class Meta:
        ordering = ('-Project_date',)
    def __str__(self):
        return self.Category

class Portfolio_details(models.Model):
    details_summary = models.TextField()

class Contacts_summary(models.Model):
    details_summary = models.TextField()




class Facts(models.Model):
    Happy_Clients = models.IntegerField()
    Projects = models.IntegerField()
    Hours_Of_Support = models.IntegerField()
    Hard_Workers = models.IntegerField()
    Facts_descprition = models.TextField()


class Skills(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField()

class SkillS_details(models.Model):
        details = models.TextField()


# Resume Details

class Summary(models.Model):
    name = models.CharField(max_length=20)
    details = models.TextField()
    address = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Email = models.EmailField()

class Education(models.Model):
    degree_name = models.CharField(max_length=300)
    details = models.TextField()
    university_name = models.CharField(max_length=100)
    year = models.DateField()


class Professional_Experience(models.Model):
    skill = models.CharField(max_length=40)
    details_list1 = models.TextField()
    details_list2 = models.TextField()
    details_list3 = models.TextField()
    details_list4 = models.TextField()
    details_list5 = models.TextField()
    city = models.CharField(max_length=40)
    year = models.DateField()

# END OF Resume Details

#Services
class Services(models.Model):
    service_offered = models.CharField(max_length=30)
    service_detail = models.TextField()

#Testimonials
class Testimonials(models.Model):
    client_name= models.CharField(max_length=30)
    client_testimony = models.TextField()
    client_occupation= models.CharField(max_length=30)
    profile =  models.ImageField(null=True, blank=True, upload_to='images/')


#Contact
class Contact(models.Model):
    address = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()


















