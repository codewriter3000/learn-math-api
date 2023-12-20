from django.contrib import admin

from modules.models import Term, Module, TestBank, Question, Submodule, Reading


# Register your models here.
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')


@admin.register(TestBank)
class TestBankAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
