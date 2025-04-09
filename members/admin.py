from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "joined_date", )


# Register your models here.
admin.site.register(Member, MemberAdmin)
