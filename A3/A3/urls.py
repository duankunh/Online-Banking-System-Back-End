"""A3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, SignupView, logout_view, \
    profile_edit_view, profile_view
from banks.views import AddBankView, AddBranchView, DisplayAllBranchesView, \
    DisplayBankView, \
    DisplayDetailBankView, DisplaySpecificBranchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', SignupView.as_view()),
    path('accounts/login/', LoginView.as_view()),
    path('accounts/logout/', logout_view),
    path('accounts/profile/view/', profile_view),
    path('accounts/profile/edit/', profile_edit_view),
    path('banks/add/', AddBankView.as_view()),
    path('banks/<int:bank_id>/branches/add/', AddBranchView.as_view()),
    path('banks/all/', DisplayBankView.as_view()),
    path('banks/<int:bank_id>/details/', DisplayDetailBankView.as_view()),
    path('banks/branch/<int:branch_id>/details/', DisplaySpecificBranchView),
    path('banks/<int:bank_id>/branches/all/', DisplayAllBranchesView)
]
