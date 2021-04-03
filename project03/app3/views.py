from django.shortcuts import render
from django.http import HttpResponse
import os

pro_dir=os.path.abspath(__file__)
project_dir=os.path.dirname(os.path.dirname(pro_dir))
template_dir=os.path.join(project_dir,"template")
html_dir=os.path.join(template_dir,"sample.html")



def project03(request):
    file=open(html_dir,'r')
    file1=file.read()
    return HttpResponse(file1)



