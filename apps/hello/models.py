import os
from django.db import models
from PIL import Image

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date = models.DateField(blank=True, null=True)
    email = models.EmailField()
    jubber = models.EmailField()
    bio = models.TextField(default='')
    other_contacts = models.TextField()
    skype = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=True):

        super(Person, self).save()
        if self.photo:
            filename = self.photo.path
            try:
                image = Image.open(filename)
                width, height = image.size
                if width > 200 or height > 200:
                    image.thumbnail((200, 200), Image.ANTIALIAS)
                    image.save(filename)
                if not os.path.isdir('uploads/photo'):
                    os.mkdir('uploads/photo', 0777)
                target = 'uploads/photo/' + filename.split('/')[-1]
                if not os.path.isfile(target):
                    os.symlink(filename, target)
            except IOError as err:
                print err
                self.photo = None
                super(Person, self).save()

    class Meta():
        db_table = 'person'


class Http_request(models.Model):
    path = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    meth = models.CharField(max_length=200, null=True)
    query = models.TextField(null=True)
    is_read = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    status_code = models.CharField(max_length=3, null=True)

    class Meta():
        db_table = 'http_request'
        ordering = ["-priority", "-date"]


class Entry(models.Model):
    action = models.CharField(max_length=12)
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
    model = models.CharField(max_length=30)
