from django.contrib import admin
from main.models import ychebniki, categories, User, Help

admin.site.register(ychebniki)
admin.site.register(categories)
admin.site.register(User)
admin.site.register(Help)