from django.shortcuts import render

def home(request):
	return render(request, 'pages/home.html')

def projects(request):
	return render(request, 'pages/projects.html')

def about(request):
	return render(request, 'pages/about.html')

def contact(request):
	return render(request, 'pages/contact.html')

def angular_myflix_case(request):
	return render(request, 'pages/cases/angular-myflix.html')

def meetapp_case(request):
	return render(request, 'pages/cases/meetapp.html')

def pokemon_case(request):
	return render(request, 'pages/cases/pokemon.html')

def promontolio_case(request):
	return render(request, 'pages/cases/promontolio.html')

def myflix_case(request):
	return render(request, 'pages/cases/myflix.html')

def jobtracker_case(request):
	return render(request, 'pages/cases/jobtracker.html')
