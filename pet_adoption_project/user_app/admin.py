from django.contrib import admin
from .models import user_details
from .models import adoption_application

admin.site.register(user_details)
admin.site.register(adoption_application)