from django.db import models
from datetime import datetime

# Create your models here.
class BOOK(models.Model):

   id = models.CharField(max_length=50, primary_key=True)
   book_name = models.CharField(max_length = 50)
   book_image = models.ImageField(upload_to='image/' )
   author = models.CharField(max_length = 50)
   publisher = models.CharField(max_length=200)
   owner_user_id = models.CharField(max_length=200)
   current_user_id = models.CharField(max_length=100)
   date_of_rent = models.DateTimeField(auto_now_add=True)
   rental_due = models.FloatField(max_length=200)
   submission_date = models.DateTimeField(auto_now_add=True)
   fine_per_day = models.IntegerField()
   deposit_by_renter = models.IntegerField()

class Meta:
    db_table = 'BOOK'
      


def __str__(self):
       return self.book_id
