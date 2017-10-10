from django.contrib import admin

from .models import Bucketlist, Items

# Register your models here.
admin.site.register(Bucketlist)
admin.site.register(Items)
