# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *

class BilletAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','photo')

admin.site.register(Billet,BilletAdmin)
