from django.shortcuts import render
from django.contrib.auth.models import User
from cars.models import Car

# Create your views here.


def main(request):
	br = []
	for i in range(1,Car.objects.count()+1):
		if i % 4 == 0 :
			br.append(i)
	return render(request,
                  'cars/cars.html',
                  {'cars': Car.objects.all(),
                  'br': br}
                  )


def superuser(request):
    User.objects.create(username='admin', is_admin=True)
    user = User.objects.get(username='admin')
    user.set_password('admin')
