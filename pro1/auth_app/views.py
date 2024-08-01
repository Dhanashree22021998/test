from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout





def signupview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a2/lv/")

    return render(request,"auth_app/sign.html",{"form":form})

def loginview(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u,password=p)
        print(user)
        if user:
            login(request,user)
            return redirect("/a1/sv/")
    return render(request,"auth_app/login.html",{})
def logoutview(request):
    logout(request)
    return redirect("/a2/lv/")

