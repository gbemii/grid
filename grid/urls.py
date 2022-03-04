"""grid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from user.views import index_view, account_view, profile_view, farm_view, investment_view, investment_detail_view, investment_form_view, setting_view, login_activity_view
from adminstrator.views import admin_index_view, investment_list, investment_detail_view, admin_profile_view, user_list_view, user_detail_view, kyc_list_view, admin_profile_setting_view, farm_views, farm_details_views, transaction_view
from Accounts.views import register

urlpatterns = [


    path('register/', register, name='register'),

    path('<int:pk>', admin_index_view, name='index'),
    path('transactions/', transaction_view, name='transation-list'),
    path('farm_list/<str:pk>/', farm_views, name='farm-list'),
    path('farmdetails/<str:pk>/', farm_details_views, name='farm_details'),
    path('adprofile/<str:pk>/',admin_profile_view, name='admin-profile'),
    path('adprofile_setting/<str:pk>', admin_profile_setting_view, name='admin-profile_setting'),
    path('kyc/', kyc_list_view, name='kyc-list'),
    path('users/', user_list_view, name='user-list'),
    path('userdetails/<int:pk>/', user_detail_view, name='userdetails'),
    path('investment_list/', investment_list, name='investment_list'),
    path('investmentdetails/<int:pk>/', investment_detail_view, name='invest_details'),
    # path('faqs/', faqs_view, name='faqs'),
    # path('terms_policy/', terms_policy_view, name='terms_policy'),


   
    
    # path('invest_form/', investment_form_view, name='investment'),
    



    path('user_index/<int:pk>', index_view, name='user_index'),
    path('profile_setting/<int:pk>/', setting_view, name='profile_setting'),
    path('login_activity/<int:pk>/', login_activity_view, name='login_activity'),

    # path('plan1/', investment_detail_view, name='investment'),
    # path('invest_form/', investment_form_view, name='investment'),


    path('plan/<int:pk>/', investment_view, name='investment'),
    path('farms/', farm_view, name='farms'),
    path('plandetails/<int:pk>/', investment_detail_view, name='investment_details'),
    path('invest_form/<int:pk>/', investment_form_view, name='investment'),
    path('profile/<int:pk>/',profile_view, name='personal'),
    path('admin/', admin.site.urls),
]
