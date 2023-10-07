from django.contrib import admin

from .models import Group, Message

@admin.register(Group)
class Group_Admin(admin.ModelAdmin):
	search_fields = ['email']
	list_display = ['title', 'idAdmin', 'isTransmission', 'isPrivate', 'archive']
	
@admin.register(Message)
class Message_Admin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['text', 'date', 'priority']