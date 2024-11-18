from django.db import models
from cloudinary.models import CloudinaryField

class Product_list(models.Model):
    Product_Image = CloudinaryField('image', null=True)  # Cloudinary storage for the image
    Product_Name = models.CharField(max_length=250, null=True)
    Product_Cat = models.CharField(max_length=250, null=True)
    Product_Description = models.JSONField(blank=True, default=list)

    def __str__(self):
        return '{}'.format(self.Product_Name)

    # No need to manually delete files because Cloudinary handles file management.
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the base class delete method


class Project(models.Model):
    Project_Image = CloudinaryField('image', null=True)  # Cloudinary storage for the image
    Project_Name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return '{}'.format(self.Project_Name)

    # No need to manually delete files because Cloudinary handles file management.
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  # Call the base class delete method
