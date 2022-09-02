from django.shortcuts import render, redirect
from .models import Book

def create(request):
    if request.method == "POST":
        im = bool(request.POST.get("impo"))
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        Book(site_name=sn, site_url=su, site_con=sc, impo=im,maker=request.user).save()
        return redirect("book:index")
    return render(request, 'bookmark/create.html')

def index(request):
    b = request.user.book_set.all()
    context = {
        "bset" : b
    }
    return render(request, 'bookmark/index.html', context)
# Create your views here.
