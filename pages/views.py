from django.shortcuts import render
from datetime import date
from .models import Student
def index(request):

    context = {
        'first_name': 'mayar',
        'last_name': 'Alhabbash',
        'student_id': '220231328',
        'address': 'KhanYounis',
        'email': '',
        'date_of_birth': date(2005, 11, 18)
    }

    return render(request, 'pages/index.html', context)

def homepage(request):
    return render(request, 'pages/homepage.html',{'student': Student.objects.first()})