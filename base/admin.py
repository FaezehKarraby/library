from django.contrib import admin

from base.models import GenreModel, AuthorModel, BookModel, AttachmentFiles

admin.site.register(GenreModel)
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(AttachmentFiles)