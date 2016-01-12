from django.contrib import admin
from models import Product, Magazine
from threads.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Magazine)
admin.site.register(Thread)
admin.site.register(Subject)
admin.site.register(Posts)