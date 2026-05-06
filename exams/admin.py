from django.contrib import admin
from .models import Exam, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'exam')
    list_filter = ('exam',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'created_at')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'exam', 'score', 'total_questions', 'submitted_at')
    list_filter = ('exam', 'participant_name')

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
