from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()
class Access_Records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)