from django.shortcuts import render


# Create your views here.
def project02(request):
    return render(request,"home.html")