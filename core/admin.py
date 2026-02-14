from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile,PickupRequest

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone','eco_points','created_at')

@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ('user','item_name','quantity','status','request_at')
    search_fields = ('user__username','item_name')
    list_filter = ('status','request_at')