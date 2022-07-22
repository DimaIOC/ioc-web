from modeltranslation.translator import register, translator, TranslationOptions
from landing.admin import AdminStatics
from landing.models import Statics


# @register(Statics)
class StaticsTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Statics, StaticsTranslationOptions)
