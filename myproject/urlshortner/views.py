from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Url
import string,random
from django.http import HttpResponseRedirect


# Create your views here.

def short_url_generator(length=6):
    characters=string.ascii_letters + string.digits
    while True:
        short_url=''.join(random.choice(characters) for _ in range(length))
        if not Url.objects.filter(short_url=short_url).exists():
            return short_url


def home(request):
    if request.method =='POST':
        long_url=request.POST.get("long_url")
        short_url=short_url_generator()


        Url.objects.create(
            long_url=long_url,
            short_url=short_url
        )

        return render(request,"home.html",{"short_url": short_url})
    return render(request, "urlshortner/home.html")


def redirect_url(request,short_url):
    try:
        url_obj=Url.objects.get(short_url=short_url)
        return HttpResponseRedirect(url_obj.long_url)
    except Url.DoesNotExist:
        return render(request,"404.html")
