from django.http import HttpResponse
from django.shortcuts import render

from .forms import CsForm

from .models import Users

# Create your views here.
def home_view(request, *args, **kwargs):

	obj = Users.objects.get(id=1)
	context = {
		'name' : obj.name,
		'email' : obj.email
	}
	return render(request, "home.html", context)

def user_create_view(request):
	form = CsForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "home.html", context)