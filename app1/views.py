from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1(request):
    html="""
        <h1 style="color:blue">Hola mundo desde app1</h1>
    """
    return HttpResponse(html)