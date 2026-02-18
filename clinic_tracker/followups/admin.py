from django.contrib import admin
from .models import Clinic, UserProfile, FollowUp, PublicViewLog


class ClinicAdmin(admin.ModelAdmin):
    readonly_fields = ("clinic_code", "created_at")

admin.site.register(Clinic, ClinicAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)

class FollowUpAdmin(admin.ModelAdmin):
    readonly_fields = ("public_token", "created_at", "updated_at")

admin.site.register(FollowUp, FollowUpAdmin)

class PublicViewLogAdmin(admin.ModelAdmin):
    readonly_fields = ("viewed_at",)

admin.site.register(PublicViewLog, PublicViewLogAdmin)