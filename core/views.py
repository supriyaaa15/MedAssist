from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == "patient":
                return redirect("patient_dashboard")
            elif user.role == "doctor":
                return redirect("doctor_dashboard")

    return render(request, "login.html")


@login_required
def patient_dashboard(request):
    if request.user.role != "patient":
        return redirect("login")
    return render(request, "patient_dashboard.html")


@login_required
def doctor_dashboard(request):
    if request.user.role != "doctor":
        return redirect("login")
    return render(request, "doctor_dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("login")