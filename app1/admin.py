from django.contrib import admin

from .models import webpage
from .models import member
# Register your models here.


admin.site.register(webpage)
admin.site.register(member)