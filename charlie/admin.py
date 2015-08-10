from django.contrib import admin
from charlie.models import SignUpEmail, SignUpInfo


class SignUpEmailAdmin(admin.ModelAdmin):
	list_display = ('date_added', 'email')
	
admin.site.register(SignUpEmail, SignUpEmailAdmin)

class SignUpInfoAdmin(admin.ModelAdmin):
	list_display = ('date_added', 'first_name', 'last_name', 'phone')

admin.site.register(SignUpInfo, SignUpInfoAdmin)