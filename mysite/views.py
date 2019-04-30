from django.shortcuts import render
from mysite.models import Work
from django.conf import settings

# Create your views here.

def home (request):
    return render(request, 'home.html')


def work (request):
    works = Work.objects.all()
    return render(request, 'work.html', {'works':works})

def contact (request):
    return render(request, 'contact.html')