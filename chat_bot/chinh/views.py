from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def error_404(req, e):
    print("404")
    return
def error_403(req, e):
    print("403")
    return
def error_400(req, e):
    print("400")
    return
def error_500(req):
    print("500")
    return

def index(req):
    print("index")
    return render(req, 'chinh/index.html', {'tit': "OK", 'text':"index"})