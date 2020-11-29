from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
      # return HttpResponse('Mohammad Javad Najafi')
      return render(request , 'about.html')

def home(request):
    # return HttpResponse('I Am Engeener Software! I love You Python! I Am Mohammad Javad Najafi, Thank You The Reading My Website!')
    return render(request , 'home.html')
