from django.db import models
from uuid import uuid4


# Create your models here.


def upload_book_image(instance, filename):
    image_file_name = "{0}-{1}".format(instance.id_book, filename)
    return image_file_name


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    book_image = models.ImageField(upload_to=upload_book_image, blank=True, null=True)
