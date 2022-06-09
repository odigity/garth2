from django.contrib import admin
from django.db import models


class Thingy(models.Model):
    name = models.CharField(max_length=50)
    qty  = models.IntegerField(default=0)


@admin.register(Thingy)
class ThingyAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'qty' ]
