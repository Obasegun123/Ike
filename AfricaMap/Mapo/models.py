from django.db import models

# Create your models here.



class Currency(models.Model):
    currency = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="currency")

    def __str__(self):
        return self.currency

class City(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="city")

    def __str__(self):
        return self.name

class Ethnic(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="ethnic")

    def __str__(self):
        return self.name

class Tourist(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="tourist")

    def __str__(self):
        return self.name

class CommonReligion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# class Tourist(models.Model):
#     name = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to="tourist")

#     def __str__(self):
#         return self.name

class LandMark(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="landmark")

    def __str__(self):
        return self.name

class Timezone(models.Model):
    timezone = models.CharField(max_length=255)
    def __str__(self):
        return self.timezone

class Demonyms(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LanguageName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Culture(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="culture", blank=True,null=True, default=None)
    def __str__(self):
        return self.name

class CapitalName(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="capital")

    def __str__(self):
        return self.name




class Country(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True,default="")
    capital = models.ForeignKey(CapitalName, on_delete=models.CASCADE, default='', null='')
    language = models.ManyToManyField(LanguageName)
    currency = models.ManyToManyField(Currency) 
    city = models.ManyToManyField(City)
    demonyms = models.ForeignKey(Demonyms, on_delete=models.CASCADE,default='', null='')
    flag = models.ImageField(upload_to="flag")
    timezone = models.ManyToManyField(Timezone)
    call_code = models.CharField(max_length=255,default='', null='')
    population = models.IntegerField()
    culture = models.ManyToManyField(Culture)
    ethnic_group = models.ManyToManyField(Ethnic)
    common_religion = models.ManyToManyField(CommonReligion)
    independence_date = models.DateField()
    landmark = models.ManyToManyField(LandMark)
    tourist = models.ManyToManyField(Tourist)
    political_history = models.CharField(max_length=255)
    spoken_language = models.FileField( upload_to ='language', default='',null=True, blank=True)
    anthem = models.FileField( upload_to='anthem')

    def __str__(self):
        return self.country