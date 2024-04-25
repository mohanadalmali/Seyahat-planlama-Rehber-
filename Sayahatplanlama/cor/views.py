from django.http import HttpResponse
from django.shortcuts import render

from cor.models import IndexPage, abouts
# Create your views here.
def index(request):
  context=dict()
  context["indexpage"] = IndexPage.objects.all()
  return render(request,'index.html', context)
def about(request):
  about=dict()
  about["abouts"] = abouts.objects.all()
  return render(request, 'about.html',about)
def blog(request):
  return render(request,'blog.html')
def contact(request):
  return render(request,'contact.html')