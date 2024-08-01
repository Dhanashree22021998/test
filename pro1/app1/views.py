from django.shortcuts import render,redirect
from . forms import BlogForm
from . models import Blog
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class Addview(LoginRequiredMixin,View):
    login_url='/a2/lv/'
    def get(self,request):
        form = BlogForm()
        return render(request,"app1/add.html",{'form':form})

    def post(self,request):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("show")
        return render(request, "app1/add.html", {'form': form})

class Showview(LoginRequiredMixin,View):
    login_url = '/a2/lv/'
    def get(self,request):
        obj = Blog.objects.all()
        return render(request,"app1/show.html",{"blog":obj})

class Updateview(LoginRequiredMixin,View):
    login_url = '/a2/lv/'
    def get(self,request,id):
        obj = Blog.objects.get(id = id)
        if obj.user == request.user:
            form = BlogForm(instance = obj)
            return render(request,"app1/add.html",{"form":form})


    def post(self,request,id):
        obj = Blog.objects.get(id=id)
        form = BlogForm(request.POST, instance=obj)
        if form.is_valid():
            blog = form.save()
            blog.user = request.user
            form.save()
            return redirect("show")
        return render(request, "app1/add.html", {"form": form})

class Deleteview(LoginRequiredMixin,View):
    login_url = '/a2/lv/'
    def get(self,request,id):
        obj = Blog.objects.get(id=id)
        return render(request,'app1/confirm.html',{"obj":obj})

    def post(self,request,id):
        obj = Blog.objects.get(id=id)
        obj.delete()
        return redirect("show")










