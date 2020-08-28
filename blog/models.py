from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Post (models.Model):
    author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title          = models.CharField(max_length = 200)
    text           = models.TextField()
    created_date   = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish (self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__ (self):
        return self.title

class EducationItem(models.Model):
    name        = models.CharField(max_length = 200)
    start_year  = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().today().year)])
    end_year    = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().today().year)])
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__ (self):
        return self.name

class TechnicalItem(models.Model):
    title   = models.CharField(max_length = 200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__ (self):
        return self.title

class WorkItem(models.Model):
    title       = models.CharField(max_length = 200)
    start_year  = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().today().year)])
    end_year    = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().today().year)])
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__ (self):
        return self.title

class OtherItem(models.Model):
    name    = models.CharField(max_length = 200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__ (self):
        return self.name