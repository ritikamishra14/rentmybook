from django.db import models


class USER(models.Model):
    id = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50, primary_key=True)
    gender = models.CharField(max_length=15)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    landmark = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=6)
    status = models.CharField(max_length=20)
    contact = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=100, default='')
    user_lat = models.FloatField()
    user_lng = models.FloatField()

    class Meta:
        db_table = 'USER'

    def __str__(self):
        return self.email_id

# Create your models here.
