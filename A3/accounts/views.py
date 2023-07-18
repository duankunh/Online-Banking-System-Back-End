from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView

from accounts.forms import LoginForm, SignupForm, UpdateUserForm


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(f"/accounts/login/")


def profile_view(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {"id": request.user.id, "username": request.user.username,
             "email": request.user.email, "first_name": request.user.first_name,
             "last_name": request.user.last_name})
    else:
        return HttpResponse('UNAUTHORIZED', status=401)


def profile_edit_view(request):
    if not request.user.is_authenticated:
        return HttpResponse('UNAUTHORIZED', status=401)
    if request.method == 'POST':
        form = UpdateUserForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(f"/accounts/profile/view/")
    else:
        initial_data = {"id": request.user.id,
                        "email": request.user.email,
                        "first_name": request.user.first_name,
                        "last_name": request.user.last_name}
        form = UpdateUserForm(None, initial=initial_data)
    return render(request, 'accounts/profile_edit.html', {"form": form})


class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        return HttpResponseRedirect(f"/accounts/login/")


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return HttpResponseRedirect(f"/accounts/profile/view/")
