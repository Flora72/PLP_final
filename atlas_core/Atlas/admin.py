from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    SurvivorProfile,
    Tag,
    Resource,
    MoodEntry,
    JournalEntry,
    UserProfile
)

# Custom User Admin (so you can see your extra fields like membership)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('membership', 'emotional_tone', 'safety_flag')}),
    )
    list_display = ['username', 'email', 'membership', 'safety_flag']

admin.site.register(CustomUser, CustomUserAdmin)

# Resource Admin
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'emotional_tone', 'is_archived', 'created_at')
    list_filter = ('emotional_tone', 'is_archived')
    search_fields = ('title', 'description')

admin.site.register(Resource, ResourceAdmin)

# Journal Entry Admin
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'sentiment_label', 'created_at')
    list_filter = ('sentiment_label', 'created_at')

admin.site.register(JournalEntry, JournalEntryAdmin)

# Mood Entry Admin
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood', 'score', 'timestamp')
    list_filter = ('mood',)

admin.site.register(MoodEntry, MoodEntryAdmin)

# Simple Registrations
admin.site.register(SurvivorProfile)
admin.site.register(Tag)
admin.site.register(UserProfile)