from django.shortcuts import render

# Create your views here.

def main_body(request):

	return render(request, "index.html")


def features(request):

	return render(request, "features.html")


def about(request):

	return render(request, "about.html")


def services(request):

	return render(request, "services.html")


def blog(request):

	return render(request, "blog.html")				


def contact(request):

	return render(request, "contact.html")	
