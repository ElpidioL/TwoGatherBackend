from django.contrib import admin

from .models import User, Role

@admin.register(User)
class User_Admin(admin.ModelAdmin):
	search_fields = ['email']
	list_display = ['name', 'email', 'status', 'lastActive', 'idRole', 'isAdmin']
	

@admin.register(Role)
class Role_Admin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name']