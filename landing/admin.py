from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Questions)
class AdminQuestions(TranslationAdmin):
    pass


@admin.register(PartnersImage)
class AdminPartnersImage(admin.ModelAdmin):
    pass


@admin.register(News)
class AdminNew(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields =('newstext',)


@admin.register(Statics)
class AdminStatics(TranslationAdmin):
    pass


@admin.register(TeamMember)
class AdminTeamMember(TranslationAdmin):
    pass


@admin.register(Report)
class AdminReports(TranslationAdmin):
    pass


@admin.register(SubtypeReporting)
class AdminSubtypeReporting(TranslationAdmin):
    pass


@admin.register(TypeReporting)
class AdminTypeReporting(TranslationAdmin):
    pass