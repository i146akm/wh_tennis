from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from . import forms


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid() and form.check_user():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                if not form.cleaned_data["remember_me"]:
                    request.session.set_expiry(0)

                return redirect('/')
    else:
        form = forms.LoginForm()

    return render(request, "login.html", {"form": form})


@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return render(request, "logout.html")
