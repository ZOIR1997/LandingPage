from django.db import models

# Create your models here.

class Customer(models.Model):
    image = models.ImageField(upload_to='images')
    fullname = models.CharField(max_length=100)
    skill = models.CharField(max_length=255, null=True)
    twitter_link = models.URLField()
    facebook_link = models.URLField()
    linkedin_link = models.URLField()
    instagram_link = models.URLField()
    youtube_link = models.URLField()
    cv = models.FileField(upload_to='files')
    phone_number = models.CharField(max_length=13)

class About(models.Model):
    body = models.TextField()
    degree = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    email = models.EmailField()
    salary = models.CharField(max_length=50)

class Development(models.Model):
    name = models.CharField(max_length=50, null=True)
    images = models.ImageField(upload_to="images_programming/", null=True)
    info = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Skills(models.Model):
    programm = models.CharField(max_length=50, null=True)
    progress = models.CharField(max_length=10, null=True)
    development_id = models.ForeignKey(Development, on_delete=models.PROTECT, null=True)

class Expericence(models.Model):
    programmer = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    info = models.TextField()

class Email(models.Model):
    email = models.EmailField()

class Service(models.Model):
    icon = models.CharField(max_length=50)
    programming = models.CharField(max_length=50)
    information = models.TextField()

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Images(models.Model):
    images = models.ImageField(null=True, blank=True, upload_to="img/")
    category_id = models.ForeignKey(Categories, on_delete=models.PROTECT)

class Testimonial(models.Model):
    fullname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/testimonial/")
    body = models.TextField()

    def __str__(self):
        return self.fullname

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email_contact = models.EmailField(max_length=100)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.email_contact


