from django.contrib import admin
from script.models import ScriptProgress,ScriptStep,Script

class ScriptStepInline(admin.TabularInline):
    model = ScriptStep
    """script progress admin """
class ScriptProgressAdmin(admin.ModelAdmin):
    """script progress admin """
class ScriptAdmin(admin.ModelAdmin):
    inlines = [ScriptStepInline]


admin.site.register(ScriptProgress,ScriptProgressAdmin)
admin.site.register(Script,ScriptAdmin)