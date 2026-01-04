from django.shortcuts import render, get_object_or_404
from .models import CaseStudy

def home(request):
	return render(request, 'pages/home.html')

def projects(request):
	return render(request, 'pages/projects.html')

def about(request):
	return render(request, 'pages/about.html')

def contact(request):
	return render(request, 'pages/contact.html')

def case_study_detail(request, slug):
	case_study = get_object_or_404(CaseStudy, slug=slug)
	return render(request, 'pages/case_detail.html', {'case_study': case_study})
