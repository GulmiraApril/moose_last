from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Post, Author


# from modeltranslation.models import checksum, FieldTranslation, trans_attr, trans_is_fuzzy_attr


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'created_at')


translator.register(Post, PostTranslationOptions)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'author_bio')


translator.register(Author, AuthorTranslationOptions)
