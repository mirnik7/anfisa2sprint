from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category

# ...и регистрируем её в админке:
admin.site.register(Category)
