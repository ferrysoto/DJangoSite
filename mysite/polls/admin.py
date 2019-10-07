from django.contrib import admin

from .models import Answers, Question

class AnswerInline(admin.StackedInline):
    model = Answers
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
         list_display = ('question_text', 'pub_date', 'was_published_recently'),
    ]
    inlines = [AnswerInline]
    list_filter = ['pub_date']

admin.site.register(Answers)
admin.site.register(Question, QuestionAdmin)
