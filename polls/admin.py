from django.contrib import admin

from .models import Poll, Question


class PollAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "start_date",
        "end_date",
        "description",
    )
    empty_value_display = "Выберите опрос"


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "text",
    )
    empty_value_display = "-пусто-"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)
