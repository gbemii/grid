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

# from django.views.static import serve
# from django.conf import settings
from django.conf.urls import url 

# from grid.settings import  STATIC_ROOT
from user.views import withdraw_form, user_password_update_view, user_profile_update_view, deposit_form, Update_plan, account_view, profile_view, farm_view, investment_view, investment_details_view, investment_form_view, setting_view, login_activity_view
from adminstrator.views import admin_password_update_view, transaction_update_view, transaction_detail_view, user_update_view, farm_update_view, investment_update_view, admin_index_view, investment_list, investment_detail_view, admin_profile_view, user_list_view, user_detail_view, kyc_list_view, admin_profile_setting_view, farm_views, farm_details_views, transaction_view
from Accounts.views import client_view, admin_view, register_view, logout_view, login_view

urlpatterns = [

    path('client/', client_view, name='clientpage'),
    path('admiin/', admin_view, name='adminpage'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    path('', admin_index_view, name='index'),
    path('admin_change_password/', admin_password_update_view, name='admin_change_password'),
    path('transactions/', transaction_view, name='transation-list'),
    path('transdetails/<str:pk>/', transaction_detail_view, name='transdetails'),
    path('farm_list/', farm_views, name='farm-list'),
    path('farmdetails/<int:pk>/', farm_details_views, name='farm_details'),
    path('adprofile/ ',admin_profile_view, name='admin-profile'),
    path('adprofile_setting/', admin_profile_setting_view, name='admin-profile_setting'),
    path('kyc/', kyc_list_view, name='kyc-list'),
    path('users/', user_list_view, name='user_list'),
    path('userdetails/<int:pk>/', user_detail_view, name='userdetails'),
    path('investment_list/', investment_list, name='investment_list'),
    path('investmentdetails/<int:pk>/', investment_detail_view, name='invest_details'),
    # path('faqs/', faqs_view, name='faqs'),
    # path('terms_policy/', terms_policy_view, name='terms_policy'),


   
    
    # path('invest_form/', investment_form_view, name='investment'),
    
    # path('Update_/<int:pk>/', _update_view, name='Update_'),
    path('Update_transaction/<int:pk>/', transaction_update_view, name='Update_transaction'),
    # path('Update_investment/<int:pk>/', investment_update_view, name='Update_investment'),
    path('Update_user/<int:pk>/', user_update_view, name='Update_user'),
    path('Update_farm/<int:pk>/', farm_update_view, name='Update_farm'),
    path('Update_investment/<int:pk>/', investment_update_view, name='Update_investment'),

    # path('user_index/', index_view, name='user_index'),
    path('profile_setting/', setting_view, name='profile_setting'),
    path('login_activity/', login_activity_view, name='login_activity'),

    # path('plan1/', investment_detail_view, name='investment'),
    

    path('deposit/', deposit_form, name='deposit'),
    path('withdrawal/', withdraw_form, name='withdrawal'),
    path('plan/', investment_view, name='investments'),
    path('Update_plan/', Update_plan, name='updateplan'),
    path('farms/', farm_view, name='farms'),
    path('plandetail/<int:pk>/', investment_details_view, name='investments_detail'),
    path('invest_form/', investment_form_view, name='investmentform'),
    path('profile/',profile_view, name='personal'),
    path('Update_profile/', user_profile_update_view, name='Update_profile'),
    path('change_password/', user_password_update_view, name='change_password'),
    path('admin/', admin.site.urls),

    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]






# urlpatterns = [

#     path('client/', client_view, name='clientpage'),
#     path('admiin/', admin_view, name='adminpage'),

#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),


#     path('<int:pk>', admin_index_view, name='index'),
#     path('transactions/', transaction_view, name='transation-list'),
#     path('farm_list/<str:pk>/', farm_views, name='farm-list'),
#     path('farmdetails/<int:farm_id>/', farm_details_views, name='farm_details'),
#     path('adprofile/<str:pk>/',admin_profile_view, name='admin-profile'),
#     path('adprofile_setting/<str:pk>', admin_profile_setting_view, name='admin-profile_setting'),
#     path('kyc/', kyc_list_view, name='kyc-list'),
#     path('users/', user_list_view, name='user-list'),
#     path('userdetails/<int:pk>/', user_detail_view, name='userdetails'),
#     path('investment_list/', investment_list, name='investment_list'),
#     path('investmentdetails/<int:pk>/', investment_detail_view, name='invest_details'),
#     # path('faqs/', faqs_view, name='faqs'),
#     # path('terms_policy/', terms_policy_view, name='terms_policy'),


   
    
#     # path('invest_form/', investment_form_view, name='investment'),
    
#     # path('Update_/<int:pk>/', _update_view, name='Update_'),
#     path('Update_transaction/<int:pk>/', transaction_update_view, name='Update_transaction'),
#     # path('Update_investment/<int:pk>/', investment_update_view, name='Update_investment'),
#     path('Update_user/<int:pk>/', user_update_view, name='Update_user'),
#     path('Update_farm/<int:pk>/', farm_update_view, name='Update_farm'),
#     path('Update_investment/<int:pk>/', investment_update_view, name='Update_investment'),

#     path('user_index/<int:pk>', index_view, name='user_index'),
#     path('profile_setting/<int:pk>/', setting_view, name='profile_setting'),
#     path('login_activity/<int:pk>/', login_activity_view, name='login_activity'),

#     # path('plan1/', investment_detail_view, name='investment'),
    

#     path('deposit/<int:pk>/', deposit_form, name='deposit'),
#     path('withdrawal/<int:pk>/', withdraw_form, name='withdrawal'),
#     path('plan/<int:pk>/', investment_view, name='investments'),
#     path('Update_plan/<int:pk>/', Update_plan, name='updateplan'),
#     path('farms/', farm_view, name='farms'),
#     path('plandetail/<int:pk>/', investment_details_view, name='investments_detail'),
#     path('invest_form/<int:pk>/', investment_form_view, name='investment'),
#     path('profile/<int:pk>/',profile_view, name='personal'),
#     path('admin/', admin.site.urls),

#     # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
#     # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
# ]

