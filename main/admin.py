from django.contrib import admin
from .models import ContactRequests, CategoryOfBusiness, Projects

admin.site.register(ContactRequests)
admin.site.register(CategoryOfBusiness)
admin.site.register(Projects)
