from django.shortcuts import render
from features.models import Info
# Create your views here.
def index(request):
    return render