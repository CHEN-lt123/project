from django.db import models

class news(models.Model):
    title = models.CharField(max_length=200) #標題
    description = models.TextField() #內文
    image = models.ImageField(upload_to='images/new5/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

