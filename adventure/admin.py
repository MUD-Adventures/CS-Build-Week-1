from django.contrib import admin

from .models import Room, Player
# Register your models here.

#to show read only fields
# class RoomAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)
#     admin.site.register(Room, RoomAdmin)

# admin.site.register(Player)

class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Player)
