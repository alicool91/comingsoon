from django.shortcuts import render

# Create your views here.


def port_create_view(request, *args, **kwargs):
	context = {}
	return render(request, 'port_create.html', context)