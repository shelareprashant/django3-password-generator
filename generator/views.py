from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%*()')
    generatedpwd = ''
    for i in range(length):
        generatedpwd += random.choice(characters)


    return render(request, 'generator/generatedpassword.html', {'password':generatedpwd})