from django.contrib import admin

from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    class Meta:
        model = Slider