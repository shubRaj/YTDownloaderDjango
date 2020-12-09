from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .ytDownloader import YouTubeDownloader
# Create your views here.
class YThome(View):
    def get(self,request,*args,**kwargs):
        return render(request,"YTDownloader/home.html")
    def post(self,request,*args, **kwargs):
        try:
            yt = YouTubeDownloader(request.POST.get("query"))
            objects = yt.links()
            context = {"objects":objects,"title":yt.title(),"thumbnail":yt.thumbnail()}
        except:
            context={}
        return render(request,"YTDownloader/home.html",context)