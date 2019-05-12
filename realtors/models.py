from django.db import models

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
