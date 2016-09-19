from django.db import models

# Create your models here.

class Car(models.Model):
	ALFA_ROMEO, BMW, LANCIA, MERCEDES_BENZ, OPEL, PORSCHE = range(1,7)
	BRAND_CHOICES = (
		(ALFA_ROMEO, 'Alfa Romeo'),
        (BMW, 'BMW'),
        (LANCIA, 'Lancia'),
        (MERCEDES_BENZ, 'Mercedes-Benz'),
        (OPEL, 'Opel'),
        (PORSCHE, 'Porsche'),
        )
	CABRIO, COUPE, SUV, LIMOUSINE, KOMBI, VAN, TRANSPORTER = range(1,8)
	CONSTRACTION_CHOICES = (
        (CABRIO, 'Cabrio'),
        (COUPE, 'Coupe'),
        (SUV, 'SUV'),
        (LIMOUSINE, 'Limousine'),
        (KOMBI, 'Kombi'),
        (VAN, 'VAN'),
        (TRANSPORTER, 'Transprter'),
        )
	MANUAL, AUTHOMATIC = range(1,3)
	TRANS_CHOICES = (
        (MANUAL, 'Manual'),
        (AUTHOMATIC, 'Authomatic'),
        )
	brand = models.PositiveIntegerField(choices=BRAND_CHOICES)
	construction =  models.PositiveIntegerField(choices=CONSTRACTION_CHOICES)
	model = models.CharField(max_length=15)
	used = models.BooleanField(blank=True, default=False)
	demonstration = models.BooleanField(blank=True, default=False)
	ez = models.DateTimeField(blank=True, null=True)
	mileage = models.IntegerField(default=0)
	power = models.PositiveIntegerField(blank=True, null=True)
	price = models.PositiveIntegerField(blank=True, null=True)
	transmission = models.PositiveIntegerField(choices=TRANS_CHOICES)
	color = models.CharField(max_length=15)
	main_photo = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_back = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_wheel = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_left = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_right = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_back_sit = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_head = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_rudder = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_player = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_monitour = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_door = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_location= models.ImageField(upload_to='photo', null=True, blank=True)
	photo_monitour = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_info = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_shop = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_monitour = models.ImageField(upload_to='photo', null=True, blank=True)
	photo_advertisement = models.ImageField(upload_to='photo', null=True, blank=True)
