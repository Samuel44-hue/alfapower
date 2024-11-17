from django.db import models
import os

class Product_list(models.Model):
    Product_Image = models.ImageField(null=True)
    Product_Name = models.CharField(max_length=250,null=True)
    Product_Cat = models.CharField(max_length=250,null=True)
    Product_Description = models.JSONField(blank=True, default=list)

    def __str__(self):
        return '{}'.format(self.Product_Name)
    
    def delete(self, *args, **kwargs):
        if self.Product_Image:
            if os.path.isfile(self.Product_Image.path):
                os.remove(self.Product_Image.path)
                super().delete(*args, **kwargs)

class Project(models.Model):
    Project_Image = models.ImageField(null=True)
    Project_Name = models.CharField(max_length=250,null=True)

    def __str__(self):
        return '{}'.format(self.Project_Name)
    
    def delete(self, *args, **kwargs):
        if self.Project_Image:
            if os.path.isfile(self.Project_Image.path):
                os.remove(self.Project_Image.path)
                super().delete(*args, **kwargs)