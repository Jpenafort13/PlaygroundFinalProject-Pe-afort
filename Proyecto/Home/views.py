from django.shortcuts import render

def home(request):
    return render(request, 'Home/index.html')

def aboutMe(request):
    return render(request, 'Home/aboutMe.html')