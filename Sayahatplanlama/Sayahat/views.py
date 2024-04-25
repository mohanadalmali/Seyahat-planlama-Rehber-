from django.shortcuts import get_object_or_404, render


def services(request):
  return render(request,'services.html')
def servicdatai(request):
  return render(request,'servicesdetia.html')