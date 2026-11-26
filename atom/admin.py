from django.contrib import admin
from atom.models import Habit, HabitCompletion


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("action", "owner", "time", "is_published")
    list_filter = ("is_published", "owner")
    search_fields = ("action", "place")


@admin.register(HabitCompletion)
class HabitCompletionAdmin(admin.ModelAdmin):
    list_display = ("habit", "completed_at")
