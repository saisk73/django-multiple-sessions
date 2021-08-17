from django.shortcuts import redirect, render
from django.views import View


def index(request):
    admin = request.session.get('admin')  
    user = request.session.get("user")
    context = {"admin": admin, "user": user}
    return render(request, "index.html", context)

class Login(View):

    def post(self, request):
        role = request.POST["role"]
        email = request.POST["email"]
        if role == "admin":
            request.session["admin"] = email
        elif role == "user":
            request.session["user"] = email
        return redirect("/")


def admin(request): 
    admin = request.session.get("admin")
    if(admin is not None):
        return render(request, "admin.html")
    else:
        return redirect("/500")

def user(request):
    user = request.session.get("user")
    if(user is not None):
        return render(request, "user.html")
    else:
        return redirect("/500")

def denied(request):
    return render(request, "denied.html")
