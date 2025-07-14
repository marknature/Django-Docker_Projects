from django.shortcuts import render
from .models import Project, Tag

# Create your views here.

def home(request):
  return render(request, 'home.html')

def contact(request):
  return render(request, 'contact.html')

def  projects(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'projects': projects,
        'tags': tags
    }
    
    return render(request, 'projects.html', context)