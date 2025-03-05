from django.shortcuts import render, redirect
from .models import Account

def home(request):
    accounts = Account.objects.all()
    return render(request, "home.html", {"accounts": accounts})

def create_account(request):
    if request.method == "POST":
        username = request.POST["username"]
        account = Account(username=username)
        account.save()
        return redirect("/")
    return render(request, "create_account.html")
