from django.db import models

# Create your models here.

    
class Upcoming(models.Model):
    month = models.CharField(max_length=25)
    year= models.CharField(max_length=25)
    event=models.TextField(max_length=500)
    location=models.CharField(max_length=25)


class News(models.Model):
    news_number =models.IntegerField()
    news_event = models.TextField(max_length=500)
    news_class = models.CharField(max_length=25, blank=True)

    def __int__(self):
        return self.news_number