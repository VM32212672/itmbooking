from django.contrib import admin
from reservationApp.models import Category, Location, Bus, Schedule, Booking,Drive
# Register your models here.
admin.site.site_header = "ITM SEMICODUCTOR ADMIN"
admin.site.site_title = "Admin Login"
class psCategory(admin.ModelAdmin):
    list_display=['name']
    list_filter = ['name']
    search_fields=['name']
admin.site.register(Category,psCategory)
class psLocation(admin.ModelAdmin):
    list_display=['location','status']
    list_filter = ['location','status']
    search_fields=['location','status']
admin.site.register(Location,psLocation)
class pBus(admin.ModelAdmin):
    list_display=['bus_number','name','seats']
    list_filter = ['bus_number','name','seats']
    search_fields=['bus_number','name','seats']
admin.site.register(Bus,pBus)
class pSchedule(admin.ModelAdmin):
    list_display=['bus','drive','depart','destination','schedule']
    list_filter = ['bus','drive','depart','destination','schedule']
    search_fields=['bus','drive','depart','destination','schedule']

admin.site.register(Schedule,pSchedule)
class pBooking(admin.ModelAdmin):
    list_display=['name','schedule']
    list_filter = ['name']
    search_fields=['name']
admin.site.register(Booking,pBooking)
class pDrive(admin.ModelAdmin):
    list_display=['name','phone']
    list_filter = ['name']
    search_fields=['name']
admin.site.register(Drive,pDrive)


