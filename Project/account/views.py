from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User



def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            return render(request, "login.html", {
                "error": "Email ya da şifre bilginiz hatalı."
            })
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["ad"]
        last_name = request.POST["soyad"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "register.html", {"error": "Kullanıcı adı kullanılmaktadır."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "register.html", {"error": "Bu email ile bağlantılı hesap zaten bulunmaktadır."})
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    return render(request,"login.html",{"success":"Hesabınız başarılı bir şekilde oluşturulmuştur."})
        else:
            return render(request,"register.html",{"error" : "Parola eşleşmiyor"})


    return render(request, "register.html")


def logout(request):
    auth_logout(request)
    return redirect("homepage")
