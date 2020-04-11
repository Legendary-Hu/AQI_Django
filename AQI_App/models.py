from django.db import models

# Create your models here.
class City_info(models.Model):
     city_id = models.AutoField(primary_key=True)
     city_name = models.CharField(max_length=40)
     aqi = models.IntegerField(null=True)
     max_poll = models.CharField(max_length=55)
     level_index = models.CharField(max_length=16)
     datetime = models.DateTimeField()

     class Meta:
          db_table = 'city_info'



class Aqi_data(models.Model):
     aqi_id = models.AutoField(primary_key=True)
     city_name = models.CharField(max_length=40,db_index=True)
     pm25 = models.IntegerField(null=True)
     pm10 = models.IntegerField(null=True)
     o3 = models.CharField(max_length=8)
     so2 = models.CharField(max_length=8)
     no2 = models.CharField(max_length=8)
     co = models.CharField(max_length=8)

     class Meta:
          db_table = 'aqi_data'

class City_local(models.Model):
     city_id = models.AutoField(primary_key=True)
     city_name = models.CharField(max_length=40)
     city_located = models.CharField(max_length=40)

     class Meta:
          db_table = 'city_position'


class data_history(models.Model):
     city_name = models.CharField(max_length=40,db_index=True)
     aqi = models.IntegerField(null=True)
     max_poll = models.CharField(max_length=55)
     level_index = models.CharField(max_length=16)
     pm25 = models.IntegerField(null=True)
     pm10 = models.IntegerField(null=True)
     o3 = models.CharField(max_length=8)
     so2 = models.CharField(max_length=8)
     no2 = models.CharField(max_length=8)
     co = models.CharField(max_length=8)
     datetime = models.DateTimeField()

     class Meta:
          db_table = 'data_history'

class city_geocode(models.Model):
     city = models.CharField(max_length=40)
     city_geocode = models.IntegerField()

     class Meta:
          db_table = 'city_geo'

class feedback(models.Model):
     name = models.CharField(max_length=20)
     email = models.CharField(max_length=20)
     phone_num = models.CharField(max_length=16)
     content = models.CharField(max_length=200)
     class Meta:
          db_table = 'feedback'