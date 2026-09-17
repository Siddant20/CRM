from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(Request):
    return HttpResponse("home")

def products(Request):
    return HttpResponse("products")

def customer(Request):
    return HttpResponse("customer")