from modeltranslation.translator import translator, TranslationOptions
from .models import Category
# from modeltranslation.models import checksum, FieldTranslation, trans_attr, trans_is_fuzzy_attr


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)
