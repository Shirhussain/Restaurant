from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Restaurant_History(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # image = models.ImageField(upload_to = "Restaurant_history/")

    class Meta:
        verbose_name = "Restaurant History"
        verbose_name_plural = "Restaurant History"

    def __str__(self):
        return self.title


class Why_choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"

    def __str__(self):
        return self.title

class Chef(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    biio = models.TextField()
    image = models.ImageField(upload_to="Chef/")

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"

    def __str__(self):
        return self.name




