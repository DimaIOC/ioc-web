from modeltranslation.translator import translator, TranslationOptions
from landing.models import *


class StaticsTranslationOptions(TranslationOptions):
    fields = ('title',)


class QuestionsTranslationOptions(TranslationOptions):
    fields = ('questiontext', 'answer',)


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('memberfullname', 'position')


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'newstext')


class ReportsTranslationOptions(TranslationOptions):
    fields = ('title',)


class SubtypeReportingTranslationOptions(TranslationOptions):
    fields = ('title',)


class TypeReportingTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Statics, StaticsTranslationOptions)
translator.register(Questions, QuestionsTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Report, ReportsTranslationOptions)
translator.register(SubtypeReporting, SubtypeReportingTranslationOptions)
translator.register(TypeReporting, TypeReportingTranslationOptions)