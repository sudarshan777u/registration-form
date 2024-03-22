from django.contrib import admin
from django.http import HttpResponse
from .models import student




class registrationAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','address','city','postal_code','highest_qualification','percentage','college','year_of_passing','course','certifications','skills','experience')  
    
    search_fields = ('name','email','mobile','address','city','percentage')  
    list_filter = ('email','course','skills') 
    
    
    actions = ['download_selected']


    

admin.site.register(student,registrationAdmin)
admin.site.site_header="HR Adminstration"

