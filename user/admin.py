from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register( Personal_info)
admin.site.register(Account)
admin.site.register(Investment_scheme)
admin.site.register(Kyc_user_info)
admin.site.register(Transactions)